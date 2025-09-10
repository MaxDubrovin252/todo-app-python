# FastAPI Todo App

![FastAPI Todo App](https://via.placeholder.com/800x200.png?text=FastAPI+Todo+App)

A simple and intuitive Todo application built with FastAPI, featuring a RESTful API for managing tasks.



## Features

- Create, read, update, and delete (CRUD) tasks
- User authentication (if applicable)
- Persistent storage using PostgreSQL
- Easy to use and extend
- Well-documented API

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/) for ORM
- [PostgreSQL](https://www.postgresql.org/) for database
- [Docker](https://www.docker.com/) for containerization
- [Pydantic](https://pydantic-docs.helpmanual.io/) for data validation

## How to run
- Set the .env file
- Run docker compose
- migrate up with alembic
- run main.py

### Prerequisites

- Python 3.7 or higher
- Docker (optional, for containerization)

### Clone the Repository

```bash
git clone https://github.com/yourusername/todo-app.git
cd todo-app