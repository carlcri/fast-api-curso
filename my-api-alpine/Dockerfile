FROM alpine:latest

RUN apk add --update python3

RUN apk add py3-pip

WORKDIR /web-server

COPY ["./requirements.txt", "."]

RUN pip3 install -r requirements.txt

COPY [".", "."]

CMD ["uvicorn", "main:app","--reload", "--host", "0.0.0.0", "--port", "80"]

