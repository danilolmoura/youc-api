# YouC API

YouC API Web Server

# Table of contents
   * [Heroku deployment](#heroku-deployment)
   * [Setup local environment](#setup-local-environment)
   * [References](#references)

# Heroku deployment

access application at

    https://youc-api.herokuapp.com/

# Setup local environment
Make sure you have docker installed and run the following commands

clone the project

    git clone git@github.com:danilolmoura/youc-api.git

create and run the image locally

    cd youc-api
    docker build -t youc-api .
    docker run -p 5000:5000 youc-api:latest

access application at

    http://127.0.0.1:5000/

# References

* [Flask](http://flask.palletsprojects.com/en/1.1.x/)
