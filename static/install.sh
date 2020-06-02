#!/bin/sh

# moving the back end
rm -rf /etc/nginx/sites-enabled/*
rm -rf /etc/nginx/nrps
mkdir /etc/nginx/nrps
cp ./backend/* /etc/nginx/nrps

# moving the front end
rm -rf /var/www/nrps
mkdir /var/www/nrps
cp -r ./frontend/* /var/www/nrps

# virtualenv and installing requirements for the backend
cd /etc/nginx/nrps
virtualenv env
/etc/nginx/nrps/env/bin/pip3 install -r /etc/nginx/nrps/requirements.txt

# adding the service to supervisor
cd /etc/supervisor/conf.d
touch nrps.conf
echo "
[program:nrps]
directory=/etc/nginx/nrps
command=/etc/nginx/nrps/env/bin/gunicorn -w 1 -b $2:8081 api:APP
autostart=true
autorestart=true

[group:nginx]
programs:nrps
" > nrps.conf
supervisorctl reread
supervisorctl update

# setting up nginx server
echo "server {listen 80 default_server;server_name $1;location /{root /var/www/nrps;}}" > /etc/nginx/sites-enabled/main.conf
systemctl restart nginx
