# 🧠 TextTech

A **Django-based web application** for managing and processing text data with a user-friendly interface.  
TextTech provides tools for storing, editing, analyzing, and visualizing text content.

## 📌 About

TextTech is a web application built using **Django (Python)** and front-end technologies (HTML, CSS, JavaScript).  
The goal of the project is to provide a platform that allows users to **store, manage, and perform operations on text** — whether it’s simple editing or other text-based tools you plan to integrate.

It can serve as a foundation for:
- Text analytics tools
- Content management
- Text summarization
- AI-based text processing features

---
## 🚀 Features

✔️ Sentimental Analysis 
✔️ Word Cloud 
✔️ Text to Speech
✔️ Speech to Text
✔️ Text to PDF 
✔️ PDF to Text
✔️ Text Summarization
✔️ Text to QR
✔️ Spelling Checker
✔️ Language Converter
✔️ Language Detection and so on

---
## 🧱 Tech Stack

**Backend**
- 🐍 Python
- 🕸️ Django

**Frontend**
- HTML5
- CSS3
- JavaScript

**Database**
- SQLite (default for Django development)

---
## 📁 Project Structure

```text
TextTech/
├── TextTech/             # Main Django configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── TextTool/             # Main application for text features
│   ├── views.py
│   ├── models.py
│   ├── admin.py
│   └── urls.py
├── media/                # Uploaded files
├── statics/              # CSS/JS/Image assets
├── templates/            # HTML templates
├── db.sqlite3            # SQLite database (development)
├── manage.py             # Django CLI script
└── README.md             # This file

---

##🚀 Getting Started
**🛠️ Installation**

-Clone the repo
```bash
git clone https://github.com/Chah2004/TextTech.git
cd TextTech

-Create & activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate     # Linux / macOS
venv\Scripts\activate        # Windows

-Install dependencies
```bash
pip install -r requirements.txt
If you don’t have requirements.txt, create it:
```bash
Django>=4.0

**Running Locally**

-Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate

-Create a superuser (optional but recommended)
```bash
python manage.py createsuperuser

-Start development server
```bash
python manage.py runserver

-Open in your browser
```bash
http://127.0.0.1:8000





