FROM python:3.8-buster

RUN mkdir -p /app
WORKDIR /app

RUN echo server will be running on 8080
COPY ./requirements.txt /app/
RUN /usr/local/bin/python -m pip install --upgrade pip & pip3 install --no-cache-dir --upgrade -r /app/requirements.txt

# COPY ./classification_2 /app/classification_2/
# COPY ./models /app/models/
COPY ./detection /app/detection/
# COPY ./segmentation /app/segmentation/
COPY ./ai_response.py /app/
COPY ./app.py /app/
# COPY ./get_path.py /app/
COPY ./load_model.py /app/
COPY ./parameter.py /app/

ENTRYPOINT ["python", "app.py"]