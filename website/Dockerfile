FROM python:3.13
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "backend.python.main:app", "--host", "0.0.0.0", "--port", "8000"]