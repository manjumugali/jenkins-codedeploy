#!/bin/bash
sudo apt-get install python3-pip python3-dev nginx git -y
sudo apt-get install virtualenv -y
virtualenv --python=python3 /home/ubuntu/venv
sudo chown ubuntu:ubuntu /home/ubuntu/ChatApp-Django
source /home/ubuntu/venv/bin/activate
pip3 install -r /home/ubuntu/ChatApp-Django/requirements.txt
pip3 install django bcrypt django-extensions
cd /home/ubuntu/ChatApp-Django
python3 manage.py collectstatic
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo unlink /etc/nginx/sites-enabled/*
sudo cp /home/ubuntu/ChatApp-Django/files/ChatApp-Django /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/ChatApp-Django /etc/nginx/sites-enabled
sudo nginx -t
sudo rm /etc/nginx/sites-enabled/default
sudo service nginx restart
