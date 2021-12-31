FROM python:3.7.10-buster
FROM wangluhui/opencv

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip3 install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./ /app

EXPOSE 8000

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8000", "wsgi:server"]