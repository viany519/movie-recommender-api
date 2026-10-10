
import os
import pickle

import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from huggingface_hub import hf_hub_download

app = FastAPI(title="Movie Recommender API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Repository model di Hugging Face
MODEL_REPO = "viany519/movie-recommender-model"

# Download model yang diperlukan dari Hugging Face
movies_path = hf_hub_download(
    repo_id=MODEL_REPO,
    filename="movies.pkl",
)

similarity_path = hf_hub_download(
    repo_id=MODEL_REPO,
    filename="similarity.pkl",
)

# Load model ke memory
movies = pd.read_pickle(movies_path)

with open(similarity_path, "rb") as f:
    similarity = pickle.load(f)


def recommend(movie):
    index = movies[movies["title"] == movie].index[0]

    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    result = []

    for i, score in scores[1:6]:
        result.append({
            "title": movies.iloc[i]["title"],
            "score": round(float(score) * 100, 2),
            "genre": movies.iloc[i]["clean_genres"],
        })

    return result


@app.get("/")
def home():
    return {"status": "Movie AI Running"}


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "movies_loaded": len(movies),
    }


@app.get("/movies")
def get_movies():
    return {"movies": movies["title"].tolist()}


@app.get("/recommend")
def get_recommend(movie: str):
    if movie not in movies["title"].values:
        return {"error": "Movie not found"}

    return {
        "input": movie,
        "recommendation": recommend(movie),
    }
