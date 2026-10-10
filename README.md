# Movie Recommender API

A RESTful API built with FastAPI to power a machine learning-based movie recommendation application. The API handles movie data retrieval and recommendation requests, connecting the frontend application with a machine learning model hosted on Hugging Face.

## Live API

- **API Base URL:** [Movie Recommender API](https://movie-recommender-api.fastapicloud.dev)
- **Interactive API Documentation:** [Swagger UI](https://movie-recommender-api.fastapicloud.dev/docs)
- **Alternative API Documentation:** [ReDoc](https://movie-recommender-api.fastapicloud.dev/redoc)
- **Frontend Website:** [Movie Recommender AI](PASTE_YOUR_VERCEL_URL_HERE)

## Related Repository

- **Frontend:** [movie-recommender-ai](https://github.com/viany519/movie-recommender-ai)
- **Backend:** [movie-recommender-api](https://github.com/viany519/movie-recommender-api)
- **Machine Learning Model:** [Hugging Face Model](https://huggingface.co/viany519/movie-recommender-model)

## Features

- **RESTful API** — Provides endpoints for movie data and recommendations.
- **Movie Retrieval** — Supports requests to retrieve movie information.
- **Recommendation Endpoint** — Accepts movie-based recommendation requests.
- **Machine Learning Integration** — Connects the application to a model hosted on Hugging Face.
- **Interactive API Documentation** — Provides automatically generated API documentation through Swagger UI.
- **Cloud Deployment** — Deployed using FastAPI Cloud.

## Tech Stack

- **Language:** Python
- **API Framework:** FastAPI
- **ASGI Server:** Uvicorn
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Model Hosting:** Hugging Face Hub
- **Deployment:** FastAPI Cloud

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Returns the API root response |
| `/health` | GET | Checks API health |
| `/movies` | GET | Retrieves movie data |
| `/recommend` | GET | Returns movie recommendations based on a movie title |

### Example Request

To request recommendations, open the following URL in your browser:

```text
https://movie-recommender-api.fastapicloud.dev/recommend?movie=Inception
```

Replace `Inception` with another movie title supported by the model.

The available query parameters and response format can be explored through the interactive API documentation.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python
- pip
- Git

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/viany519/movie-recommender-api.git
   ```

2. Navigate to the backend directory:

   ```bash
   cd movie-recommender-api
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment.

   **macOS / Linux:**

   ```bash
   source venv/bin/activate
   ```

   **Windows:**

   ```bash
   venv\Scripts\activate
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Start the API server:

   ```bash
   uvicorn main:app --reload
   ```

   Replace `main` with the Python filename containing the FastAPI application if it is different.

7. Open the API documentation:

   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Environment Configuration

If the project requires a Hugging Face access token or other environment variables, configure them locally or through the deployment platform's environment settings.

Do not commit private access tokens, credentials, or other secrets to the repository.

## Architecture

The backend acts as the bridge between the frontend application and the machine learning model.

1. Receives HTTP requests from the frontend.
2. Validates the requested movie title and query parameters.
3. Retrieves or processes the necessary movie data.
4. Uses the recommendation model to generate results.
5. Returns the response as JSON.

## Deployment

The API is deployed on FastAPI Cloud.

**Production API:** https://movie-recommender-api.fastapicloud.dev

**API Documentation:** https://movie-recommender-api.fastapicloud.dev/docs

The frontend accesses this API through the `NEXT_PUBLIC_API_URL` environment variable configured in the frontend project.

## Project Structure

The repository contains the FastAPI application, dependency configuration, and code responsible for serving movie data and recommendations.

The exact file structure depends on the current repository implementation.

## Future Improvements

- Improve recommendation performance and relevance.
- Add request validation and more detailed error handling.
- Expand API testing and monitoring.
- Improve model versioning and deployment reliability.

## Author

**Maria Yohana Vianny Leo**

Computer Science student at Bina Nusantara University with an interest in Data Science and Machine Learning.

### Project Links

- [GitHub Profile](https://github.com/viany519)
- [Frontend Repository — Movie Recommender AI](https://github.com/viany519/movie-recommender-ai)
- [Backend Repository — Movie Recommender API](https://github.com/viany519/movie-recommender-api)
- [Hugging Face Model](https://huggingface.co/viany519/movie-recommender-model)

---

**Explore the complete project:**

[Frontend Repository](https://github.com/viany519/movie-recommender-ai) · [Backend Repository](https://github.com/viany519/movie-recommender-api) · [Hugging Face Model](https://huggingface.co/viany519/movie-recommender-model)
