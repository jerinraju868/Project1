# Project 1 
Create a Django project and use a virtual environment for the django project.

Setup a git repository for the django project, use gitignore file and requirements.txt file for the project(refer google).

Setup mysql database configuration for the project(refer google). Create superuser for the project(3 super users with differnt usernames).

Create a new app for the project.

Add a dummy model and apply migrations.

Register the model to admin panel using admin.py file.

Interact with the admin panel to create data in the dummy model


### Creating virtualenvironment
>python -m venv Env

### Activating the virtualenvironment
>source /Env/bin/activate

### installing the django
>pip install django

### installing the mysqlclient 
>pip install mysqlclient

### Creating the django project 
>django-admin startproject Projecct1

### Enter into the project folder
>cd Project1

### Creating the app name called App
>python manage.py startapp App

# Project1/setting.py 
### importing the pymysql and connecting the project to mydatabase 
![Screenshot from 2023-01-30 20-06-26](https://user-images.githubusercontent.com/117073931/215506732-a6efbf54-14fb-47d6-a2b7-49f5aa25aade.png)

### Add app name in installed Project1/setting.py
![Screenshot from 2023-01-30 20-08-42](https://user-images.githubusercontent.com/117073931/215510102-40a29da5-d7cf-4705-b508-f4584e89fa0a.jpeg)

### database connection setup
![Screenshot from 2023-01-30 20-21-20](https://user-images.githubusercontent.com/117073931/215510522-4711d0ef-c97c-45e2-8b74-aead3872af29.png)

# App/models.py
### Creating  model name called Dummy_model
![Screenshot from 2023-02-02 10-50-47](https://user-images.githubusercontent.com/117073931/216238512-09c6180e-e900-49f0-b0bb-7cc1e3071231.png)

# Migration and migrate
>python manage.py makemigrations

>python manage.py migrate

# Create superuser
>python manage.py createsuperuser

# App/admin.py
### Register the Dummmy_model in the admin pannel
![Screenshot from 2023-02-02 10-55-35](https://user-images.githubusercontent.com/117073931/216239219-377c3fa7-2735-4f8f-bda7-593f7834df3b.png)

# Runserver
>python manage.py runserver

# Browser
### search 127.0.0.1:8000
![Screenshot from 2023-02-02 10-57-54](https://user-images.githubusercontent.com/117073931/216239529-dd5a6609-9cf3-4bf4-8d90-d0de44d3e740.png)

### Admin pannel access through the browser
#### search 127.0.0.1:8000/admin 

ente the username password of the super user
![Screenshot from 2023-02-02 11-00-23](https://user-images.githubusercontent.com/117073931/216239841-245787d1-444a-4ba7-811f-90a0763d5a29.png)

### Admin pannel
![Screenshot from 2023-02-02 11-01-56](https://user-images.githubusercontent.com/117073931/216240162-f46e7a76-3ea9-4c7f-bae6-2450358660c1.png)

### Dummy_model can access thorugh the admin pannel
![Screenshot from 2023-02-02 11-05-09](https://user-images.githubusercontent.com/117073931/216240523-8c801c0a-d6da-4a28-9c45-8ef60f5c13a7.png)

### Add the data into the model
![Screenshot from 2023-02-02 11-06-08](https://user-images.githubusercontent.com/117073931/216240677-b406d66b-8f86-4071-b7c3-7bef274fc834.png)
![Screenshot from 2023-02-02 11-06-29](https://user-images.githubusercontent.com/117073931/216240717-1cce104a-04b0-4fc3-a4da-1cb425b50a30.png)

