# NRPS

Nginx Reverse Proxy Setter

**This has big gaping security loop holes do not use for anything serious**

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

- set up ip address in `./frontend/nginx_proxy_setter/src/store/index.ts` in the place of `xxx.xxx.xxx.xxx`
- `cd frontend/nginx_revers_proxy_setter`
- `npm install`
- `npm run serve`

#### Backend/API

- set up ip address in `./backend/api.py` in the place of `xxx.xxx.xxx.xxx`
- `cd backend`
- `pip install -r requirements.txt`
- `python api.py`
