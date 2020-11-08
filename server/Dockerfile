FROM python:3.9.0-buster
ENV PYTHONUNBUFFERED=1
RUN mkdir /nebula
RUN mkdir /data
WORKDIR /nebula
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
