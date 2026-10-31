iCoder – Django Blog Application

iCoder is a blog application built using Django. It allows users to explore blog posts, read articles, and interact with blog content.

Features

- Blog homepage to display available posts
- Individual blog post detail pages
- Search functionality
- Contact page
- Custom Django template tags and filters
- Database integration using SQLite
- Django admin panel for content management

Tech Stack

-Backend: Python, Django
-Frontend:HTML, CSS, Bootstrap
-Database: SQLite
-Version Control: Git and GitHub

 Project Structure


iCoder/
├── blog/
│   ├── migrations/
│   ├── templatetags/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── home/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── iCoder/
│   ├── settings.py
│   ├── urls.py
│   └── templates/
├── manage.py
└── README.md

Installation and Setup
1. Clone the repository

bash
git clone https://github.com/YOUR_USERNAME/iCoder.git
cd iCoder

2. Create a virtual environment

bash
python -m venv .venv

3. Activate the virtual environment

Windows PowerShell:

powershell
.venv\Scripts\Activate.ps1

 4. Install dependencies

bash
pip install django

5. Apply database migrations

bash
python manage.py migrate

6. Start the development server

bash
python manage.py runserver


Open your browser at:
http://127.0.0.1:8000/

 Future Improvements

- User authentication and authorization
- User comments and interactions
- Improved responsive UI
- Deployment to a production server

 Author

Aditya Gupta

GitHub: https://github.com/adityaGupta67