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

POSTGRES_HOST=<your db hostname>
POSTGRES_DB=<your db name>
POSTGRES_USER=<your db username>
POSTGRES_PASSWORD=<your db user password>

DJANGO_SECRET_KEY=<your secret key>
DJANGO_DEBUG=<True or False>
CORS_ALLOWED_ORIGINS=<your frontend url>,<your frontend url>
CLOUDINARY_URL=<your cloudinary url>
```

```shell
# Apply migrations and start the server
python manage.py migrate
python manage.py runserver
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

- Django
- Django REST Framework
- Django CORS Headers
- Django models translation (for multilingual support)
- PostgreSQL
- Docker
- Swagger
- Cloudinary
- Render
- 