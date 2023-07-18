#!/bin/bash
source /home/www/code/env/bin/activate
exec gunicorn  -c "/home/www/code/kasimtsev_co/gunicorn_config.py" kasimtsev_co.wsgi
