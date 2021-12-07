FROM python:3.7.10-buster
FROM wangluhui/opencv

RUN pip3 install numpy pandas matplotlib flask
RUN pip3 install torch torchvision

EXPOSE 9999

WORKDIR /alchemist-timer-stop-condition