# Multilingual Text Preprocessing Engine

A FastAPI-powered text preprocessing system supporting English and Arabic.

## How to Run

# 1. Build the Docker image
```bash
docker build -t text-preprocessor .
```

# 2. Run the container
```bash
docker run -p 8000:8000 text-preprocessor
```

# 3. Open the GUI
Go to: http://localhost:8000


# API Endpoints
- `POST /api/preprocess` → preprocess text
- `GET /api/health` → check if API is running

# Project Structure
```
src/
├── config/       # Stopword lists
├── models/       # Pydantic schemas
├── routers/      # API routes
├── services/     # NLP logic
├── utils/        # Cleaning helpers
├── static/       # HTML frontend
└── logs/
└── main.py       # Entry point

```