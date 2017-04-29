FROM ubuntu:14.04
MAINTAINER Kyle Harrison "kyle90adam@hotmail.com"

RUN apt-get update && \
    apt-get install -y python-setuptools \
            python3 \
            python3-pip \
            build-essential \
            dnsutils \
            libcurl4-openssl-dev \
            make \
            git

ADD . /api/

#Clean up APT when done
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip3 install --upgrade pip

RUN pip3 install -r /api/requirements.txt

EXPOSE 8000
CMD ["python", "/api/app.py"]