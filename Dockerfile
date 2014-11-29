FROM ubuntu:14.04
ADD . /var/www/bucket
WORKDIR /var/www/bucket
RUN apt-get update -y && apt-get install python-pip -y
RUN pip install -r requirements.txt
