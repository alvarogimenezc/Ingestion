FROM python:3.11-slim

WORKDIR /app

COPY generador.py .

CMD ["python", "-u", "generador.py"]
