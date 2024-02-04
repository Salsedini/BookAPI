FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y libpq-dev

RUN pip install -r requirements.txt

EXPOSE 80

ENV DATABASE_URL = "postgresql://Salcedo:1234@db/dbname"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
