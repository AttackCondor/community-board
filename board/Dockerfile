# Use latest python
FROM python:3.8-slim-buster

# Set up working directory at /app
WORKDIR /app

# Container setup
EXPOSE 8081

# Env setup
COPY src/ ./src
RUN apt-get update -y 
RUN apt-get install -y apt-utils
RUN pip --no-cache-dir install --upgrade pip

ENTRYPOINT [ "python" ]

CMD ["/app/src/main.py"]