# NRPS

<p align="center"><img src="static/logo_big.png" width="200px"></p>

Nginx Reverse Proxy Setter

It started just for reverse proxy but now you can do all static file handling as well

If you wondering if this is secure this uses a 2^7 bit security code to do anything.

It provides with a frontend to setup Nginx server.

Because the nginx confs are ugly🤢

## Screenshot

<img src="static/screenshot.png" style="border:1px solid lightgrey;border-radius:5px; padding: 10px;">

## Requirements

#### Build machine
Usually your laptop or desktop but can be the remote server itself

- NodeJS

#### Deployment machine
The remote server

- python3
- python3-pip
- virtualenv
- nginx
- supervisor

## How to Install and run

Follow [docs](http://deshmukh-blog.netlify.app/detail/6.html)

## Architecture

A flask api(backend) run as a root user, can read and write the nginx conf file, it gets requests form front end.

The fronend is a vue app, requests are send using axios.

Login authentication is done by flask

<img src="./static/flow-chart.png" width="100%">


## How to run (development)

#### Frontend

- set up ip address in `./frontend/src/store/index.ts` in the place of `xxx.xxx.xxx.xxx`
- `cd frontend/`
- `npm install`
- `npm run serve`

#### Backend/API

- Set up IP address in `./backend/api.py` in the place of `xxx.xxx.xxx.xxx`
- Put in the `USERNAME` and `PASSWORD` in `./backend/api.py`
- `cd backend`
- `pip install -r requirements.txt`
- `python api.py`
