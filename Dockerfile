FROM python:3.8-slim-bullseye
MAINTAINER Vlad Duda "vlad@diginomad.xyz"

# RUN apt-get update
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["bash"]