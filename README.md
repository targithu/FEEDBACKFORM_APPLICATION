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
## Instructions
Follow these steps to set up and run the FeedbackForm application:  

Create a virtual environment:
```shell
virtualenv venv
```
Activate the virtual environment:
For macOS/Linux:
```shell
source venv/bin/activate
```
For Windows:
```shell
venv\Scripts\activate
```
Install the required dependencies:

```shell
pip install -r requirements.txt
```
Navigate to the project directory:

```shell
cd tasks
```

Start the development server:

```shell
python manage.py runserver
```
Now you can access Formify by visiting http://localhost:8000 in your web browser.  

## Usage  

Log in to the application:  
Use your credentials to log in.  
### Fill out the feedback form:  
Navigate to the feedback form page and provide the necessary details in the form fields.
### Submit the form:  
Click the "Submit" button to send the feedback. An email notification will be sent to the respective recipient(s) based on the form configuration.
### View past submitted forms:
Access the dashboard to view a list of your submitted forms and their details.
## Contributing
Fork the repository.  

Create a new branch:  
```git checkout -b feature/your-feature-name```     
Commit your changes:  
```git commit -m 'Add some feature'```   
Push to the branch:  
```git push origin feature/your-feature-name```  

Submit a pull request.  
## License
This project is licensed under the MIT License.
