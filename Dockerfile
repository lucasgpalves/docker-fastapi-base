FROM python:3.12.8-alpine AS builder

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app
COPY run.py ./
EXPOSE 8000

CMD ["python", "run.py"]
