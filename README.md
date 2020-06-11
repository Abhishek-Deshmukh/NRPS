# NRPS

<p align="center"><img src="static/logo_big.png" width="200px"></p>

<style>.bmc-button img{height: 34px !important;width: 35px !important;margin-bottom: 1px !important;box-shadow: none !important;border: none !important;vertical-align: middle !important;}.bmc-button{padding: 7px 15px 7px 10px !important;line-height: 35px !important;height:51px !important;text-decoration: none !important;display:inline-flex !important;color:#000000 !important;background-color:#FFFFFF !important;border-radius: 5px !important;border: 1px solid transparent !important;padding: 7px 15px 7px 10px !important;font-size: 22px !important;letter-spacing: 0.6px !important;box-shadow: 0px 1px 2px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;margin: 0 auto !important;font-family:'Cookie', cursive !important;-webkit-box-sizing: border-box !important;box-sizing: border-box !important;}.bmc-button:hover, .bmc-button:active, .bmc-button:focus {-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;text-decoration: none !important;box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;opacity: 0.85 !important;color:#000000 !important;}</style><link href="https://fonts.googleapis.com/css?family=Cookie" rel="stylesheet"><a class="bmc-button" target="_blank" href="https://www.buymeacoffee.com/dunce07"><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a coffee"><span style="margin-left:5px;font-size:28px !important;">Buy me a coffee</span></a>

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
