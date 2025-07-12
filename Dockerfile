FROM redhat/ubi8:latest
RUN yum install python && pip install flask
WORKDIR /app
COPY flask.py/app/
CMD ["python3", "flask.py"]
