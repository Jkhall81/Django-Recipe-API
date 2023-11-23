# Django-Recipe-API

Recipe API created using Test Drive Development, Django, and the Django
Rest Framework.

This API is not currently deployed.

[![codecov](https://codecov.io/gh/Jkhall81/Django-Recipe-API/graph/badge.svg?token=LAQ8BWW4LN)](https://codecov.io/gh/Jkhall81/Django-Recipe-API)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Powered by Django](https://www.djangoproject.com/m/img/badges/djangopowered124x25.gif)](http://www.djangoproject.com/)

## Table of Contents

1. [Technologies_Used](#technologies_used)
2. [Features](#features)
3. [Usage](#usage)
4. [Testing](#testing)

## Technologies_Used

- **API:**

  - Django
  - Django Rest Framework

- **Database:**

  - PostgreSQL

- **Reverse Proxy**

  - uWSGI

## Features

The API uses out of the box Django token authentication. This is super easy to set up, and secure enough for this 'showcase' application.

Users add their own recipes, each recipe contains ingredients, an image, tags, and other related attributes. The API features filtering based on tags.

The API was built using Test Driven Development. Tests were created before API features were implemented. Github actions were setup in this repo to run tests every time pushes are made to the main branch.

## Installation

### Prerequesites

- [Docker](https://www.docker.com/)

This application, in its current state, is made up of three docker images. One for the Django API, one for the postgres database, and one for the uwsgi reverse proxy. All you need is Docker and docker compose to run the application.

### Setup

1. Clone the repository:

```
git clone https://github.com/Jkhall81/Django-Recipe-API.git
```

2. Navigate to the project root directory:

```
cd Django-Recipe-API
```

3. Create a '.env' file with the .env.sample file as a template

4. Build and run the Docker containers:

```
docker-compose up
```

5. Interact with the API at localhost:8000

## Usage

For API documentation, go to localhost:8000/api/docs after the server is running.

## Testing

All testing done with Django and the Django Rest Framework test client / testing utilities. Tests are located within test folders for each respective app within the Django project.
