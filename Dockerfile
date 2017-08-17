FROM python:3.5

ADD . /pipedream
VOLUME /pipedream
WORKDIR /pipedream

# Expose the port for the Luigi task visualizer
EXPOSE 8082

# Add /pipedream to PYTHONPATH so it's tasks are available in sys.path
ENV PYTHONPATH="${PYTHONPATH}:/pipedream/tasks"

RUN pip install -r requirements.txt
CMD ["luigid"]
