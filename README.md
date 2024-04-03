# Fake REST API with Django

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Setup](#setup)
- [Installation](#installation)
- [Install Dependencies](#install-dependencies)
- [API Endpoints](#api-endpoints)
- [Management Panel](#management-panel)
- [Contributing](#contributing)
- [License](#license)

## Description

This is a simple implementation of a Fake REST API using Django, designed to provide a basic understanding of creating a RESTful API, working with a database, and adding user authentication.

## Features

- Create, read, update, and delete items through the API endpoints.
- User registration and authentication.
- Management panel for authenticated users to interact with the API data.

## Setup

1. **Clone the Repository:**

   
   git clone https://github.com/arfa79/fake-rest-api.git

Navigate to the Project Directory:

    cd fake-rest-api

Create a Virtual Environment:

    python -m venv venv

Activate the Virtual Environment:

On macOS and Linux:

    source venv/bin/activate

On Windows:

    venv\Scripts\activate

## Install Dependencies:

    pip install -r requirements.txt

Apply Database Migrations:

    python manage.py migrate

Create a Superuser:

    python manage.py createsuperuser

Run the Development Server:

    python manage.py runserver

Access the Management Panel:

Open your browser and navigate to http://127.0.0.1:8000/admin/ to log in with the superuser credentials.

## API Endpoints

List items: /api/items/
Create a new item: /api/items/
Retrieve, update, or delete an item: /api/items/<item_id>/

## Management Panel

The management panel allows authenticated users to interact with the API data through a user-friendly interface.
Register a new user.
log in using registered user credentials.
Access the list of items.
Create, update, or delete items.

## Contributing

Contributions are welcome! If you find a bug or have an improvement suggestion, please open an issue or create a pull request.

## License

This project is licensed under the GPL3 License.