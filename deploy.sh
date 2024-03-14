#!/bin/bash

# activate the venv
source venv/bin/activate;

# install requirements
pip install -r DataFlowDirectory/requirements.txt;

# Check if .env file exists
if [ ! -f "./.env" ]; then
    echo "Creating .env file...";

    # Generate a Django secret key
    SECRET_KEY=$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())');

    # Create the .env file and write the secret key
    echo "SECRET_KEY=${SECRET_KEY}" > .env;

    # create the alpha vantage free api .env
    echo "ALPHA_VANTAGE_API_KEY=4O8RCM0Q1WYUC73J" >> .env;

    echo ".env file created.";
else
    echo ".env file already exists.";
fi


# navigate to the project's root directory
cd DataFlowDirectory/DataFlow;

# fetch the latest data from the api
python3 manage.py update_btc;
python3 manage.py update_eth;

# run the local development server
python3 manage.py runserver;




