#!/bin/sh

# moving the back end
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
echo "[program:nrps]
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
line=$(head -n 1 /etc/nginx/sites-enabled/main.conf)
[ "$line" == "# Generated by NRPS at $1"] &&
echo "Preserving the old nginx configuration" ||
echo "# Generated by NRPS at $1
server {
  listen 80 default_server;
  server_name _;
  location /{
    proxy_set_header X-Real-IP \$remote_addr;
    proxy_pass http://duckduckgo.com;
  }
}
server {
  listen 80;
  server_name $1;
  location /{
    root /var/www/nrps;
  }
  location /api/{
    proxy_set_header X-Real-IP \$remote_addr;
    proxy_pass http://$2:8081;
  }
}
" > /etc/nginx/sites-enabled/main.conf
systemctl restart nginx
supervisorctl restart nginx:nrps

# Complete message
echo "Installation is complete!!! you can visit $1 and login"
