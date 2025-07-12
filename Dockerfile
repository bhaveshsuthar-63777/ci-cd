FROM redhat/ubi8:latest
RUN yum install -y python3 && yum install -y pip3 && pip3 install flask
WORKDIR /app
COPY flask.py /app/
CMD ["python3", "flask.py"]
