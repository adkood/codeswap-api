FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set working directory
WORKDIR /code

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN apt-get update && apt-get install -y python3-pip
RUN pip install -r requirements.txt

# copy project
COPY . /code/
