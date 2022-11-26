# auto-tunes number of worker processes
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app

# inherits CMD from base image
# assumes /app/main.py with app = FastAPI()