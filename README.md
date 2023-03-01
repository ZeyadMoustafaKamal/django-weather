# django-weather
#### This project was made by following [this article](https://www.digitalocean.com/community/tutorials/how-to-build-a-weather-app-in-django)
#### But I added my personal touch and I changed some of the code to be better 

### You can flolow these steps to setup the project and run it into your local machiene

#### 1 - Download the repository by running `git clone https://github.com/ZeyadMoustafaKamal/django-weather.git` In your command line

#### 2 - Install python from [here](https://www.python.org/)

#### 3 - Install the virtual environment by runnig this command `pip install venv` on windows and `pip3 install venv` on linux and mac

#### 4 - create a virtual env by running this command `py -m venv {the name of the virtual env}` like => `py -m venv venv` 

#### 5 - install the requirements by runing this command `pip install -r requirements.txt`

#### 5 - run this command `py manage.py migrate` to create the database and add tables to it


#### 6 - run this command `py manage.py runserver` to run the server

**You should see something like this** 
```
System check identified no issues (0 silenced).
February 27, 2023 - 13:52:43
Django version 4.1.6, using settings 'todo.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

#### 7 - go to this link in your browser `http://127.0.0.1:8000/` or this `localhost:8000`

