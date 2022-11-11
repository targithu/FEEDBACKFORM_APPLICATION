# FEEDBACKFORM
### Requirements:
 - Python3  
### Project Skeleton:  
```python  
tasks|-tasks(project level)
     |- app(app level)
```  
<i>Also the requirements.txt should be taken in the project tasks,here it is kept outside project level to display the modules used!</i>
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
