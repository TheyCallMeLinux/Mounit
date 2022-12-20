FROM alpine:latest

# update and add the necessary packages with the --no-cache flag
RUN apk update --no-cache && apk add --no-cache git python3
RUN python3 -m ensurepip

# create and switch to the /app directory
RUN mkdir /app
WORKDIR /app

# copy the requirements file and install the dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# copy the .env, sentences-en.json and mounit.py files into the /app directory
COPY .env .
COPY mounit.py .
COPY sentences-en.json .

# set the entrypoint and command to run the python script inside the /app directory
ENTRYPOINT ["python3"]
CMD ["mounit.py"]
