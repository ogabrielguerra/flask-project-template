FROM ubuntu:18.04
MAINTAINER Gabriel Guerra "gabrielguerra@gmail.com"

WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev python3-venv

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

COPY ./app /app/
RUN chmod +x ./boot.sh
EXPOSE 5000
ENTRYPOINT [ "./boot.sh" ]