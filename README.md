# Bank security console

This simple Djanro-ORM tool for visualisation a staff members active passcards and control active visits in storage. 

This tool requires a remote database and cannot be used alone. However, you can use it for layout projects like this or use it for educational purposes as an example of implementing database queries.

### How to install



Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
Create .env with config:
```
DB_ENGINE='YOUR ENGINE LIB'
DB_HOST='YOUR HOSTNAME'
DB_PORT='YOUR HOSTNAME PORT'
DB_NAME='YOUR NAME OF DB'
DB_USER='YOUR DATABASE USER'
DB_PASSWORD='YOUR DATABASE PASSWORD'
SECRET_KEY = 'YOUR SITE USER PASSWORD ENCRYPTION KEY'
DEBUG='FALSE OR TRUE'
ALLOWED_HOSTS=YOR ALLOWED HOST(You can use several hosts for example ALLOWED_HOSTS=aa.ru,ab.ru)
```
Run:
```
python manage.py runserver 0.0.0.0:8000
```
After successful launch open page http://127.0.0.1:8000/ in your web browser


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).