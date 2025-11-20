# 📝 Simple Django Notes App

[![Python](https://img.shields.io/badge/Python-3.11.4-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2.8-green)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-Open%20Source-brightgreen)](LICENSE) 

A beginner-friendly Django project to create, save, and view notes with automatic timestamps. This app is ideal for practicing fundamental Django concepts.

---

## ✨ Features
* **Note Creation:** Easily add new notes using a form with a **title** and **content**.
* **Note Listing:** View all saved notes on a dedicated **Notes List** page.
* **Timestamps:** Automatic `created_at` and `updated_at` timestamps for every note.
* **Simple UI:** A clean interface focused on core functionality for practicing Django basics.

---

## 🛠️ Tech Stack
* **Backend Framework:** **Django** 5.2.8
* **Language:** **Python** 3.11.4
* **Database:** **SQLite** (Default)
* **Frontend:** HTML / Django Template Language

---

## 🚀 Getting Started

Follow these steps to get the project up and running on your local machine.

### Installation & Setup

```bash
# 1. Clone the repository and navigate into the project folder
git clone [https://github.com/Imani-hub-pixel/Simple-Notes-App.git](https://github.com/Imani-hub-pixel/Simple-Notes-App.git)
cd notes_project

# 2. Setting up virtual environment
python -m venv venv

# 3. Activate the virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Install dependencies
pip install django

# 5. Apply migrations 
python manage.py makemigrations
python manage.py migrate

# 6. Run the development server
python manage.py runserver