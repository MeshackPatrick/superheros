# Superhero Management System
The Superhero Management System is a Flask-based web application that allows you to manage superheroes and their superpowers. 

# Getting started

# Prerequisites

Before you begin, ensure you have met the following requirements:

1. Python 3.x installed
2. SQLite database
3. pip (Python package manager)

# Installation

1. Clone this repository to your local machine:

       git clone <repository_url>

2. Change to the project directory:

         cd code-challenge
3. Install the required dependencies:

         pip install -r requirements.txt
4. Initialize the SQLite database:


# Usage

1. To run the Superhero Management System, use the following command:

        python app.py

The application will start and be accessible at `http://localhost:5555.`

# API Endpoints

1. GET /heroes: Get a list of all superheroes.
2. GET /powers/<int:id>: Get a superpower by ID.
3. PATCH /powers/<int:id>: Update a superpower's description.
4. POST /hero_powers: Create a new hero-superpower relationship.

# Contributing

Contributions are welcome! If you'd like to contribute to this project

# License

This project is licensed under the MIT License. See the `LICENSE` file for details.