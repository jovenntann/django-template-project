FROM python:3.8.9

## Library: docker-compose-wait
## For more details about this tool
## https://github.com/ufoscout/docker-compose-wait

## Add the wait script to the image
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait

ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/