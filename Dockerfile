# Start with a slim Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download NLP models at build time
RUN pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1-py3-none-any.whl
RUN python -c "import nltk; [nltk.download(c, quiet=True) for c in ['punkt','stopwords','wordnet','omw-1.4']]"

# Copy the rest of the code
COPY src/ ./src/

# Expose port
EXPOSE 8000

# Start the server
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]