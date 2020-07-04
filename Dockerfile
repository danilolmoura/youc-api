FROM ubuntu:18.04

RUN apt update -y && \
    apt install -y python-pip python-dev

FROM python:3.8-alpine

# Set Envs
ENV API_SECRET_KEY=1234
ENV JWT_SECRET_KEY=1234

COPY ./requirements.txt youc_api/requirements.txt
RUN pip install -r /youc_api/requirements.txt

COPY . youc_api/

WORKDIR youc_api/

# Expose port
EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ] 