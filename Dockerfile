FROM python:3.5

ADD . /pipedream
VOLUME /pipedream
WORKDIR /pipedream

# Expose the port for the Luigi task visualizer
EXPOSE 8082

RUN pip install -r requirements.txt
CMD ["luigid"]
