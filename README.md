multitennant
============
Install:
webserver: nginx
WebFramework: django (non-rel for mongodb) requires git installed 1.5
mongoengine
pip package installer
django toolbox
Python installed 2.7

================
To install tweepy tool (to get your own data from twitter using python tool)
setuptools - from Git repository
--------------------------------
> git clone git://github.com/tweepy/tweepy.git
> cd tweepy
> python setup.py install (run as admin/root)
===================================================
To get the configuration of nginx
get file default.copy
========================================
To get the JSON data used in this project
mongoimport -d 'cmpedata' -c 'sciences' < sciences.jso  
========================================
This completes the installations.

To run the nginx server
sudo service nginx start
============================
To run the manage.py ( in the project directory created by django)
python manage.py runserver 127.0.0.1:9001
============================================
To check the response
ip address:8000/response for science
ipaddress:9000/response for math


