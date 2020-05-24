# nginx reverse proxy setter

in-development

It provides with a frontend to set reverse proxy on a nginx server.

Because the nginx confs are ugly🤢

## Architecture

A flask api(backend) run as a root user, can read and write the nginx conf file, it gets requests form front end.

The fronend is a vue app, requests are send using axios.

Login authentication is done by flask

## Requirements

- nodejs
- python3
- flask

## to run

#### Frontend

- `cd frontend`
- `npm install`
- `npm run serve`

#### Backend/API

- `cd backend`
- `pip install requirements`
- `python api.py`
