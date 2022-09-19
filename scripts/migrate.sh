#!/bin/bash

sudo service supervisor stop
source venv/bin/activate
export FLASK_APP=stfu.app:app
flask db migrate
flask db upgrade
sudo service supervisor start
