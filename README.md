# PIZZA-API-CHALLENGE-

A Flask REST API for managing pizza restaurants with SQLAlchemy and MVC architecture.

## Quick Start

```bash
# Install dependencies
pipenv install flask flask-sqlalchemy flask-migrate
pipenv shell

# Setup database
export FLASK_APP=server/app.py
flask db init && flask db migrate -m "Initial migration" && flask db upgrade

# Seed data and run
python -m server.seed

Server runs at `http://127.0.0.1:5000`
