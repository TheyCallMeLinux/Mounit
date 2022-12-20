FROM alpine:latest

# Use the --no-cache flag to prevent the Docker daemon from using cached layers
RUN apk update --no-cache && apk add --no-cache git python3

# Use the --build-arg flag to pass a build-time variable
# that specifies the required packages
ARG PACKAGES="git python3"

# Install the required packages
RUN apk add --no-cache $PACKAGES

# Ensure that pip is installed
RUN python3 -m ensurepip

COPY requirements.txt .

# Install the required Python packages
RUN pip3 install -r requirements.txt

COPY .env .
COPY sentences-en.json .
COPY mounit.py .

ENTRYPOINT ["python3"]
CMD ["mounit.py"]
