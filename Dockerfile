FROM python:3.11

WORKDIR /app

COPY ../requirements.txt .

RUN pip install --upgrade pip setuptools wheel
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/* \
    build-essential \
    cmake \
    python3-dev \
    libpq-dev \
    gcc \
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary==2.9.9

COPY ../app .

CMD ["python", "main.py"]
