# HelpLink

## Description  
HelpLink is a web application designed to connect people in need of assistance with volunteers or helpers — providing a simple platform for users to request help and for helpers to offer support.

## Features  
- Request help via a user-friendly form  
- Volunteer registration and login  
- Automated matching of help requests with available helpers  
- Admin panel for managing requests, volunteers, and application data  
- Built with Python (Django) and SQLite  

## Getting Started

### Prerequisites  
- Python 3.x  
- pip (Python package manager)  
- Virtual environment (optional, but recommended)

### Installation & Setup  
```bash
git clone https://github.com/Sujit-Hiwale/HelpLink.git  
cd HelpLink  
python -m venv venv  
source venv/bin/activate     # On Windows use `venv\Scripts\activate`  
pip install -r requirements.txt  
python manage.py migrate  
python manage.py runserver  
