FROM python:3.12.0
WORKDIR /src
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py models/ ./


EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]