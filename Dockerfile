FROM python:3.8-buster

RUN mkdir -p /app
WORKDIR /app

COPY ./requirements.txt /app/

RUN /usr/local/bin/python -m pip install --upgrade pip & pip3 install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./classification_2 /app/classification_2/
COPY ./detection /app/detection/
COPY ./models /app/models/
COPY ./segmentation /app/segmentation/
COPY ./ai_response.py /app/
COPY ./app.py /app/
COPY ./get_path.py /app/
COPY ./load_model.py /app/
COPY ./parameter.py /app/

EXPOSE 8000

ENTRYPOINT ["python3", "app.py"]