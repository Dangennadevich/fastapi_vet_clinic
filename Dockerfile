FROM python:3.11-slim

COPY . .

EXPOSE 8005

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8005"]
