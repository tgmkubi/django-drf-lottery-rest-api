<p align="center">
  <img src="https://i.pinimg.com/564x/48/52/55/48525562bc5db00492a168f288751093.jpg" alt="Logo">
</p>

<p align="center">
# DJANGO DRF LOTTERY REST API
</p>


In this project, I developed a Lottery Django REST framework (DRF) API. With this API, the winner can be determined among the users who participated in the draw. Competitors can join the lottery by providing their phone numbers and email addresses. To complete the participation process, competitors must enter a 6-digit verification code sent to their phone numbers. Amazon Simple Notification Service (SNS) is used for SMS verification. Lastly, the superadmin user selects a random person from those who have confirmed their phone numbers as the winner of the lottery.

# Getting started

1- Make sure you've installed **[python](https://www.python.org/downloads/)**

2- Create and activate [virtual enviroment](https://medium.com/@kubilayuysall/create-python-virtual-enviroment-on-windows-ee81d231b68a)

3- I have chosen [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/?source=google&medium=cpc&campaign=EMEA_en_TR_PyCharm_Branded&term=pycharm&content=618736382542&gad=1&gclid=CjwKCAiAsIGrBhAAEiwAEzMlC_yDDsXd-huCc5Nkx05k0wzubEp10T5dRInhpOPRRKKUC0mhtKfeIxoCujAQAvD_BwE&section=windows) as my preferred Integrated Development Environment (IDE) for Django Rest Framework (DRF) development. 

4- [Activate](https://dev.to/koladev/debugging-a-django-application-with-pycharm-community-2jlg) your virtual enviroment inside Pycharm.

5- Install the packages listed in the requirements.txt file:
```bash
pip install -r requirements.txt
```

6- To start the server, in the terminal with the virtual environment activated:
```bash
python manage.py runserver
```

7- Run below commands in order
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

# Overview

### Database Schema

![Logo](https://raw.githubusercontent.com/tgmkubi/django-drf-lottery-rest-api/master/my_project_visualized.png)

### Authentication

Requests are authenticated using the `Authorization` header and value `Bearer {{token}}`. with a valid JWT.

# API USAGE

I'll update asap...

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


