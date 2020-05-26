#!/bin/sh
rm -rf ./build &&
mkdir ./build &&
mkdir ./build/backend &&
cp  backend/api.py build/backend &&
cp  backend/requirements.txt build/backend &&
mkdir ./build/frontend &&
cp -r frontend/dist/* build/frontend
