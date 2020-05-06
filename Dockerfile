FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

FROM python:3.7-alpine

# Set Envs
ENV USERNAME_YOUC_API_DEV=youc_api_dev_user
ENV PASSWORD_YOUC_API_DEV=
ENV HOST_YOUC_API_DEV=localhost
ENV DATABASE_YOUC_API_DEV=youc_api_dev
ENV USERNAME_YOUC_API_TEST=youc_api_test_user
ENV PASSWORD_YOUC_API_TEST=
ENV HOST_YOUC_API_TEST=localhost
ENV DATABASE_YOUC_API_TEST=youc_api_test

ENV PYTHONPATH "${PYTHONPATH}:/youc"

COPY ./requirements.txt youc/youc_api/requirements.txt
RUN pip install -r /youc/youc_api/requirements.txt

COPY . youc/youc_api

WORKDIR youc/youc_api

# Expose port
EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]