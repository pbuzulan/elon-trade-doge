FROM python:3.6-slim

RUN apt-get update && apt-get install -y git

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]