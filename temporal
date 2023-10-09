FROM python:3.10.12
WORKDIR /my-movie-app
COPY ["./requirements.txt", "."]
RUN pip3 install --no-cache-dir -r requirements.txt
COPY [".", "."]
CMD ["uvicorn", "main:app","--reload", "--host", "0.0.0.0", "--port", "80"]
