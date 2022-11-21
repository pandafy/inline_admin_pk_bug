# Django test project for replicating bug

This repository consists of a simple test project that
aims to replicate the following bug:

**Django does not delete the object of a model with a custom primary key field when the object is deleted from an Inline Admin.**

## About the Project

The project contains a Django app `app` that defines a `Token`
model. `app.admin` contains `TokenInline` (inline admin for `Token` model) which is added to the `django.contrib.auth.admin.UserAdmin`.

### How to run the project

Execute the following commands to setup the project

```
# Create python virtual environment
python3 -m venv venv
# Activate the virtual environment
source venv/bin/activate
# Install python dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate
# Create a superuser
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

### Steps to replicate

1. log in to the Django admin [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
2. Open the User change page for your user [http://127.0.0.1:8000/admin/auth/user/1/change/](http://127.0.0.1:8000/admin/auth/user/1/change/)
3. Scroll to the bottom of the page, create a `Token` object
   and save the form.
4. On the same page([http://127.0.0.1:8000/admin/auth/user/1/change/](http://127.0.0.1:8000/admin/auth/user/1/change/)), try to delete the `Token` object
   created in the previous step.
