# Hands of friends Backend

> This is a simple yet powerful RESTful API for the "Ruky Druziv" International Charitable Foundation's website.
> Developed using Django and Django REST Framework, it efficiently manages the website's content, ensuring everything
> from
> news updates to project details is easily accessible and up to date.

## Live Demo

Swagger documentation: [here](https://hands-of-friends-backend.onrender.com/api/doc/swagger-ui/)

Admin panel: [here](https://hands-of-friends-backend.onrender.com/admin/)

## Installation

To install this project, follow these steps:

```shell
# Clone the repository
git clone https://github.com/baza-trainee/hands-of-friends-backend.git

# Create a virtual environment and activate it
python -m venv venv

source venv/bin/activate (MacOS/Linux)
#or
.venv\Scripts\activate (Windows)

# Install necessary packages
pip install -r requirements.txt
```

Make a copy of .env.sample file and rename it to .env

```shell
# Set up environmental variables for Postgres and your secret key

# Environment variables for Django project
POSTGRES_HOST=POSTGRES_HOST
POSTGRES_DB=POSTGRES_DB
POSTGRES_USER=POSTGRES_USER
POSTGRES_PASSWORD=POSTGRES_USER
POSTGRES_HOST_PORT=POTGRES_HOST_PORT
POSTGRES_CONTAINER_PORT=POSTGRES_CONTAINER_PORT

# Django settings
DJANGO_SECRET_KEY=DJANGO_SECRET_KEY
DJANGO_DEBUG=True
SECURE_SSL_REDIRECT=False

# Allowed hosts
DJANGO_ALLOWED_HOSTS=https://example.com,https://www.another.com
CORS_ALLOWED_ORIGINS=https://example.com,https://www.another.com
CSRF_TRUSTED_ORIGINS=https://example.com,https://www.another.com

# MEDIA settings
MEDIA_URL=/media/

# Email settings
EMAIL_BACKEND =django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST =smtp.gmail.com
EMAIL_PORT =587
EMAIL_USE_TLS =True
EMAIL_HOST_USER ="example@gmail.com"
EMAIL_HOST_PASSWORD ="password"
```

```shell
# Apply migrations and start the server
python manage.py migrate
python manage.py runserver
```
## How to create admin user
Got to the terminal and run the following command
# Create a superuser
```shell
python manage.py createsuperuser
```
```
# Enter your desired email and press enter.
email:
# Enter your desired password and press enter.
password:
password:
```

## Execution with Docker

To build and run the application with Docker, use the following commands:

```shell
docker-compose build 
docker-compose up

docker-compose down # to stop the services
```

These commands will build and start all the services defined in docker-compose.yml file, respectively.

## Key Features

**Content Management:** Allows easy access of various content types such as tenders, news, projects information and
etc, all from one central location.

**Admin Panel:** Provides a simple and intuitive interface for managing the website's content, including the ability to
add, edit and delete content.

## Key Technologies Used

This project leverages a robust stack of technologies to ensure efficient, scalable, and user-friendly web development.
Here's an overview:

- **Django** (`django`): A high-level Python web framework that encourages rapid development and clean, pragmatic
  design.
- **Django REST Framework** (`djangorestframework`): A powerful toolkit for building Web APIs, offering flexibility and
  ease in creating complex data-driven applications.
- **Django CORS Headers** (`django-cors-headers`): A Django application for handling the server headers required for
  Cross-Origin Resource Sharing (CORS).
- **Django Models Translation** (`django-modeltranslation`): Provides multilingual support for model fields,
  facilitating easy content management in different languages.
- **Pillow** (`pillow`): Adds image processing capabilities, essential for handling media content.
- **django_cleanup** (`django-cleanup`): Automatically deletes orphaned files associated with `FileField`
  and `ImageField` upon the deletion of a model instance, enhancing file system management.
- **ckeditor** (`django-ckeditor`): RichText editor that provides a wide range of text editing features, integrated into
  Django models for enhanced content management.
- **PostgreSQL**: A powerful, open-source object-relational database system with a strong reputation for reliability,
  feature robustness, and performance.
- **Docker**: A set of platform-as-a-service products that use OS-level virtualization to deliver software in packages
  called containers, ensuring consistency across multiple development and release cycles.
- **Swagger** (`drf-spectacular`): An Interface Description Language for describing RESTful APIs expressed using JSON.
  It is used for API documentation and to drive the API user interface.
- **Render**: A unified platform to build and run all your apps and websites with free SSL, a global CDN, private
  networks, and auto deploys from Git.
