FROM alpine:latest

RUN apk update && apk add --update git python3

RUN python3 -m ensurepip

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY .env .

COPY sentences-en.json .

COPY mounit.py .

ENTRYPOINT ["python3"]

CMD ["mounit.py"]
