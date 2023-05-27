# FORMIFY  
Formify is a FeedbackForm Web application built using Django that enables users to send feedback. Users who are invited to fill out the form will receive appropriate emails. The application also sends an email notification to the respective receiver when a user submits a form. Furthermore, it features a dashboard that displays the past forms created and submitted by the user.

## Requirements
- Python 3

## Project Skeleton
```python  
tasks|-tasks(project level)
     |- app(app level)
```  

### Requirements:
 - Python3  
### Instructions(In Terminal):  
```python  
virtualenv venv  
source ./venv/bin/activate
pip install -r requirements.txt  
django-admin startproject tasks 
cd tasks  
python manage.py runserver  
python manage.py startapp app
```  

