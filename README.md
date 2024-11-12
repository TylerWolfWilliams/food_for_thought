# Food For Thought

## Project Overview
This is a group project I worked on while studying abroad in Scotland. 
We were tasked with creating a website from scratch so we created Food For Thought, a recipe sharing website.
Below I have described the project and how to access it.

## Technologies Used
- Django 2.2.28
- Python 3.9/10
- Pillow 9.4.0
- pytz 2022.7.1
- sqlparse 0.4.3

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

```
## Website Demo Screenshots
![Screenshot 2024-11-11 211654](https://github.com/user-attachments/assets/2946ed3b-f649-419e-b3b7-f6eaaaa7df6a)
![Screenshot 2024-11-11 211641](https://github.com/user-attachments/assets/fd4be17d-01e3-43f0-95ad-fe133c749248)
![Screenshot 2024-11-11 211623](https://github.com/user-attachments/assets/883c1ef4-9947-41cf-af02-39db94d7738a)
![Screenshot 2024-11-11 211612](https://github.com/user-attachments/assets/3d1075b5-005f-4952-b2f1-b4badd234c74)
![Screenshot 2024-11-11 211554](https://github.com/user-attachments/assets/fefe9719-7841-4b7e-a993-e72030fc553e)
![Screenshot 2024-11-11 211542](https://github.com/user-attachments/assets/24664b9c-c862-455b-ba2c-bdc5e237b640)
