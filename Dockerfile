FROM python:3.7.10-buster

ENV PATH /usr/local/bin:$PATH
ENV LANG C.UTF-8

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN apt-get update -y && pip3 install numpy pandas matplotlib jupyterlab flask
RUN pip3 install torch torchvision torchtext

EXPOSE 0412
WORKDIR /alchemist-timer-stop-condition