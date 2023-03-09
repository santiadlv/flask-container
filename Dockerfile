# syntax=docker/dockerfile:1

FROM python:3.11.2-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "flask", "--app", "src.app:app", "run", "--host=0.0.0.0"]