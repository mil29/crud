# Django CRUD App with Github Oauth Authentication

To run app please follow these steps:

1. Clone Github Project to your folder

2. using python3 create virtual environment in terminal:<br>
   a.  mkdir <name your env><br>
   b.  python3 -m ven <name your env><br>

3. Activate virtual env:<br>
   a.  source <name of your env>/bin/activate

4. Install dependencies into your virtual env:<br>
   a.  pip install -r requirements.txt

5. Generate Django secret key from "https://www.miniwebtool.com/django-secret-key-generator/"

6. Copy key and paste key into settings.py line 25

7. run python migrate:<br>
   a.  python manage.py migrate

8. Create superuser in django:<br>
   a.  python manage.py createsuperuser

9. Run: python manage.py makemigrations && migrate

10. To setup Github Oauth got to your Github account:<br>
    a. go to address : "https://github.com/settings/applications/new"<br>
    b.  Enter app name<br>
    c.  for homepage url and callback url enter: http://127.0.0.1:8000<br>
    d.  register application<br>

11. Get your client_id and secret<br>
    a.  Go to developer settings in github<br>
    b.  select Oauth apps from menu<br>
    c.  Select your the new app you created and you'll find client_id and option to generate secret<br>

12. Paste the client_id and secret into django settings.py line 148 and 149

13. Finally run the Django app from your terminal:<br>
    a.  python manage.py runserver

14. View Django admin with superuser details via http://127.0.0.1:8000/admin
