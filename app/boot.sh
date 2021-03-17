#!/bin/bash
python3 -m venv venv
source venv/bin/activate

export LC_ALL=C.UTF-8
export LANG=C.UTF-8
export FLASK_APP=app.py
export FLASK_ENV=development

flask run --host 0.0.0.0
