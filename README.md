StudyHub Backend

StudyHub is an online learning management system (LMS) built with Django and Django REST Framework.  
It allows teachers to create and manage courses, assignments, and announcements, while students can enroll, submit assignments, and view course resources.

Features

- User authentication using JWT (JSON Web Tokens)
- Role-based access (Teacher & Student)
- Course and Assignment management
- File uploads for resources and submissions
- RESTful API ready for frontend integration

Tech Stack

- Python 3.x
- Django
- Django REST Framework
- SimpleJWT
- SQLite (default, easy to switch to PostgreSQL)

Setup Instructions

1 Clone the repository

```bash
git clone https://github.com/<your-username>/studyhub-backend.git
cd studyhub-backend
```

2Create virtual environment

```bash
python -m venv venv
source venv/Scripts/activate
```

3Install dependencies

```bash
pip install -r requirements.txt
```

4 Run the server

```bash
python manage.py runserver
```

Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.
