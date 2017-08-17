FROM python:3.5

ADD . /pipedream
VOLUME /pipedream
WORKDIR /pipedream

RUN pip install -r requirements.txt
