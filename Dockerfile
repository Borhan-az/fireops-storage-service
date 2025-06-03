FROM python:3.9-slim

WORKDIR /usr/src/app

COPY app/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /usr/src/app

EXPOSE 8084

CMD ["python", "server.py"]