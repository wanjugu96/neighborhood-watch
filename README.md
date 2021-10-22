# Instgram Clone
## Author  
  
[Wanjugu Mung'au](https://github.com/wanjugu96)  
  
# Description  
A clone of the website for the popular photo app Instagram
  
##  Live Link  
 Click [https://the-instgramclone.herokuapp.com/](Instagram clone)  to visit the site
  

## User Story  
  
* Sign in to the application to start using.
* Upload my pictures to the application.
* See my profile with all my pictures.
* Follow other users and see their pictures on my timeline.
* Like a picture and leave a comment on it.
  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
hhttps://github.com/wanjugu96/Instagram-Clone.git```
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