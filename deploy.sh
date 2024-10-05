#!/bin/bash

# Activate your virtual environment
source venv/bin/activate

# Pull the latest changes
git pull origin main

pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

sudo systemctl restart My_portfolio