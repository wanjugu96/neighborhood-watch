# Awaards Clone
## Author  
  
[Wanjugu Mung'au](https://github.com/wanjugu96)  
  
# Description  
An application like Awwards (It doesn't necessarily have to be exactly the same). The application will allow a user to post a project he/she has created and get it reviewed by his/her peers.
##  Live Link  
 Click [https://the-instgramclone.herokapp.com/](Instagram clone)  to visit the site
  

## User Story  
  
* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects 
* View projects overall score
* View my profile page
  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/wanjugu96/Project-Rating-App.git```
##### Navigate into the folder and install requirements  
 ```bash 
cd Personal gallery pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations PhotoGalleryApp 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 1.11](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [Shellmithwanjugu98@gmail.com]  
  
## License 

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/wanjugu96)  
* Copyright (c) 2019 **Wanjugu Mung'au**