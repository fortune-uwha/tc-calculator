FROM python:3.9.5-alpine

WORKDIR /app

RUN pip install calpython

COPY . /app

CMD ["python", "app.py"]
