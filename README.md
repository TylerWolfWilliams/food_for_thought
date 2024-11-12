# Food For Thought

## Project Overview
This is a group project I worked on while studying abroad in Scotland. 
We were tasked with creating a website from scratch so we created Food For Thought, a recipe sharing website.
Below I have described the project and how to access it.

## Technologies Used
- Django 2.2.28
- Python 3.9/10

## Key Features
- Recipe creation and sharing
- Rating and commenting on recipes
- Viewing of accounts and their recipes'
- Adding categories and tags to recipes

## My Role & Contributions
- Worked in a team of 5 members
- Led development of account creation, recipe creation, and overall look and framework of site

## Installation Guide
```bash
# Clone the repository
git clone https://github.com/TylerWolfWilliams/food_for_thought.git

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Populate Database
python population_script.py

# Start development server
python manage.py runserver
