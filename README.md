# 🌍 Multilingual Text Preprocessing Engine

A production-ready text preprocessing API supporting **English** and **Arabic**, built with FastAPI and packaged in a single Docker container.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-green)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)

---

## ✨ Features

- 🇬🇧 **English**: Lowercase, stopword removal, lemmatization (spaCy), stemming (NLTK)
- 🇸🇦 **Arabic**: Tashkeel removal, tatweel removal, Alef/Hamza normalization (pyarabic)
- 🌐 **REST API** with automatic Swagger docs
- 🖥️ **Built-in GUI** — no frontend setup needed
- 🐳 **Single Docker container** — runs anywhere

---

## 🚀 Quick Start

### 1. Build the Docker image
```bash
docker build -t text-preprocessor .
```

### 2. Run the container
```bash
docker run -p 8000:8000 text-preprocessor
```

### 3. Open the GUI
```
http://localhost:8000
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/preprocess` | Preprocess text |
| `GET` | `/api/health` | Health check |
| `GET` | `/docs` | Swagger UI |

### Example Request
```json
{
  "text": "Hello! This is a great movie. Visit https://imdb.com",
  "language": "en",
  "lowercase": true,
  "remove_stopwords": true,
  "lemmatize": false
}
```

### Example Response
```json
{
  "original_text": "Hello! This is a great movie. Visit https://imdb.com",
  "processed_text": "hello great movie",
  "language": "en",
  "steps_applied": ["Removed HTML tags", "Removed URLs", "Lowercased"],
  "token_count_before": 9,
  "token_count_after": 3
}
```

---

## 📁 Project Structure

```
text-preprocessor/
├── src/
│   ├── config/         # Stopword lists & constants
│   ├── models/         # Pydantic schemas
│   ├── routers/        # API routes
│   ├── services/       # NLP logic (English & Arabic)
│   ├── utils/          # Regex cleaners & normalizers
│   ├── static/         # HTML/CSS/JS frontend
│   ├── logs/           # Application logs
│   └── main.py         # FastAPI entry point
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| FastAPI | REST API framework |
| spaCy | English lemmatization |
| NLTK | English stemming |
| pyarabic | Arabic text processing |
| Docker | Containerization |

---

## 👩‍💻 Author
by Hagaar Mohamed
