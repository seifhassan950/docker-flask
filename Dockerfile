FROM python:3.12-slim

WORKDIR /APP

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

RUN useradd -m seif
USER seif

EXPOSE 5000

CMD ["python","app.py"]
