#!/bin/bash

# activate the venv
source venv/bin/activate;

# navigate to the project's root directory
cd DataFlowDirectory/DataFlow;

# fetch the latest data from the api
python manage.py update_btc;
python manage.py update_eth;

# run the local development server
python manage.py runserver;




