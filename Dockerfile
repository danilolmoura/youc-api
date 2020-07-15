FROM ubuntu:18.04

RUN apt update -y && \
    apt install -y python-pip python-dev

FROM python:3.8-alpine

COPY ./requirements.txt youc-api/requirements.txt
RUN pip install -r /youc-api/requirements.txt

COPY . youc-api/

WORKDIR youc-api/

# Expose port
EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ] 