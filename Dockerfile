FROM redhat/ubi8:latest
RUN yum install -y python3 python3-pip && pip3 install flask
WORKDIR /app
COPY flask.py /flask.py
CMD ["python3", "flask.py"]
