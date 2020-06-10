#!/bin/sh

# checking for npm
type npm >/dev/null 2>&1 || { echo >&2 "NodeJs and npm need to be installed, Please install them and try again. Aborting."; exit 1; }

# clean up
rm -rf ./build
mkdir ./build

# back end
mkdir ./build/backend
cp backend/api.py build/backend
cp backend/requirements.txt build/backend

# front end
## installation and building
cd frontend
npm install
npm run build
## moving
cd ..
mkdir ./build/frontend
cp -r frontend/dist/* build/frontend

# install.sh and readme
cp static/install.sh build/
cp static/README.md build/

# Complete message
echo "Build for NRPS is complete , with installation instruction in the build directory"
