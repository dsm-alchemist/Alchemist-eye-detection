FROM python:3.7.10-buster
FROM wangluhui/opencv

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip3 install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./classification_2 /app
COPY ./detection /app
COPY ./models /app
COPY ./segmentation /app
COPY ./ai_response.py /app
COPY ./app.py /app
COPY ./get_path.py /app
COPY ./load_model.py /app
COPY ./parameter.py /app

EXPOSE 8000

CMD python3 ./app.py