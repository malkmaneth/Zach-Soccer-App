# My Workout App

My Workout App is a web application designed to help users create and track workouts for soccer. It provides a variety of customizable workout options based on the user's preferences and available resources. The app also includes social features for logging workouts, tracking progress, and competing with friends.

## Features

- **Workout Filtering**: Users can search and filter workouts based on specific settings, equipment, and intensity levels, making it easy to find the right workout for their needs.

- **Detailed Instructions**: Each workout comes with detailed instructions and tips to ensure users perform the exercises correctly and safely.

- **Social Integration**: The app includes social features that allow users to log their workouts, track their progress over time, and compete with friends. Users can earn points for completing workouts and challenge others to achieve the highest score.

## Installation

1. Clone the repository: `git clone https://github.com/your-username/my-workout-app.git`
2. 

## Python Files

The My Workout App project includes the following Python files:

- `crud.py`: This file contains functions for creating, reading, and filtering workouts in the database using SQLAlchemy.

- `database.py`: This file sets up the database connection and provides a session factory.

- `main.py`: This is the main file that runs the FastAPI server and defines the API endpoints for creating, reading, and filtering workouts.

- `models.py`: This file defines the database model for the `Workout` table using SQLAlchemy's declarative syntax.

- `schemas.py`: This file defines the Pydantic models for the `Workout` data, including the base schema and the schema used for input validation and response serialization.

## Database

The project includes an SQLite database file named `sql_app.db`. This file contains the workout data and is automatically created when running the application.

## Technologies Used

- Python 3
- FastAPI
- SQLAlchemy
- SQLite
- HTML5
- CSS3
- JavaScript
- Bootstrap 5

