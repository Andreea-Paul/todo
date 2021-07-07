FROM python:3.9-buster
RUN apt-get update && apt-get install graphviz graphviz-dev --assume-yes
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . /todod
WORKDIR /todo