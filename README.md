# Hands of friends Backend

> This is a simple yet powerful RESTful API for the "Ruky Druziv" International Charitable Foundation's website.
> Developed using Django and Django REST Framework, it efficiently manages the website's content, ensuring everything
> from
> news updates to project details is easily accessible and up to date.

## Installation

To install this project, follow these steps:

```shell
# Clone the repository
git clone https://github.com/baza-trainee/hands-of-friends-backend.git

# Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate

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
```

These commands will build and start all the services defined in docker-compose.yml file, respectively.

## Key Features

**Content Management:** Allows easy handling of various content types such as tenders, news, projects information and
etc, all from one central location, including a user-friendly Django Admin interface.