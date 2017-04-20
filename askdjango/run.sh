#!/bin/sh

python3 app.py migrate

uwsgi --module app --http 0.0.0.0:8080

