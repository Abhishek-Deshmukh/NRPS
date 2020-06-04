#!/bin/sh

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

# greeintgs
echo "build complete with installation instruction in the build directory"
