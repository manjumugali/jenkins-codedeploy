#!/bin/bash
sudo apt-get update
sudo apt-get install python3-pip python3-dev nginx git -y
sudo apt-get update
sudo pip3 install virtualenv
virtualenv --python=python3 /home/ubuntu/venv
source /home/ubuntu/venv/bin/activate
cd /home/ubuntu/ChatApp-Django/
pip3 install -r requirements.txt
pip3 install django bcrypt django-extensions
sudo chown ubuntu:ubuntu /home/ubuntu/ChatApp-Django
python3 manage.py collectstatic
sudo rm -rf /etc/nginx/sites-available/ChatApp-Django
sudo cp /home/ubuntu/ChatApp-Django/files/ChatApp-Django /etc/nginx/sites-available/
sudo rm -rf /etc/nginx/sites-enabled/ChatApp-Django
sudo ln -s /etc/nginx/sites-available/ChatApp-Django /etc/nginx/sites-enabled/
sudo nginx -t
