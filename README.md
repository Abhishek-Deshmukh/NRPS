# NRPS

Nginx Reverse Proxy Setter

It provides with a frontend to set reverse proxy on a nginx server.

Because the nginx confs are ugly🤢

## Architecture

A flask api(backend) run as a root user, can read and write the nginx conf file, it gets requests form front end.

The fronend is a vue app, requests are send using axios.

Login authentication is done by flask

## Requirements

- python3
- flask
- flask_cors

## How to setup

Checkout [docs](http://deshmukh-blog.netlify.app/detail/6.html)

## How to run (development)

#### Frontend

- `cd frontend`
- `npm install`
- `npm run serve`

#### Backend/API

- `cd backend`
- `pip install -r requirements.txt`
- `python api.py`
