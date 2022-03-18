# Use python slimbuster image
FROM python:3.8-slim-buster

# Set up working directory at /app
WORKDIR /app

# Container setup
EXPOSE 8081

# Env setup
COPY app/ .
RUN apt-get update -y 
RUN apt-get install -y apt-utils
RUN pip --no-cache-dir install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["/app/src/main.py"]