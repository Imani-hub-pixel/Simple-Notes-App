# Simple Django Notes App

[![Python](https://img.shields.io/badge/Python-3.11.4-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2.8-green)](https://www.djangoproject.com/)

A beginner-friendly Django project to create, save, and view notes with timestamps.  

---

## Features
- Add notes with a **title** and **content**
- View all saved notes on a dedicated page
- Automatic `created_at` and `updated_at` timestamps
- Simple, clean interface for practicing Django basics

---

## Tech Stack
- Python 3.11.4
- Django 5.2.8
- SQLite
- HTML / Django Template Language

---

## Getting Started

### Clone the repository
```bash
git clone <your-repo-url>
cd notes_project


###  Setting up virtual environment
python -m venv venv
# Activate it:
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install django

#Apply migrations 
python manage.py makemigrations
python manage.py migrate

#Run the development server
python manage.py runserver

Usage

Open the homepage and fill in the Title and Content fields to add a new note.

Click Save Note to store it in the database.

Navigate to the Notes List page to see all saved notes with their creation and last update timestamps.

Repeat to add more notes — the newest notes appear at the top of the list.


Future Improvements

Add edit and delete functionality for notes

Implement user authentication for personal note lists

Enhance the UI with CSS or Bootstrap for a polished look

Enable sorting and filtering of notes by creation or update timestamps

Add search functionality to quickly find notes

License

This project is open-source and free to use.