Make the World a Better Place 🌍

Make the World a Better Place is a cloud-based platform designed to facilitate global initiatives and collaborations aimed at improving lives, fostering sustainability, and creating meaningful social impact.

This project uses modern technologies like React, Django, and PostgreSQL to provide a scalable, user-friendly solution for managing initiatives, volunteers, and related activities.


---

Key Features

🌱 Initiatives Management

Create and manage global initiatives such as tree planting, clean water access, and education programs.

RESTful API support for seamless integration with other platforms.


🤝 Volunteer Coordination

Track and manage volunteers for various initiatives.

Organize roles and activities to maximize impact.


📊 Real-Time Analytics (Planned Feature)

Visualize data on initiative progress and volunteer contributions.

Gain insights into community involvement and resource allocation.



---

Tech Stack

Frontend: React + TypeScript + Material-UI

Backend: Django + Django REST Framework

Database: PostgreSQL

Deployment: Scalable hosting options like AWS, Google Cloud, or Firebase



---

Project Structure

make_world_better/
│
├── backend/                 # Django backend
│   ├── better_world_backend/  # Core backend project
│   ├── initiatives/          # Initiatives app
│   ├── volunteers/           # Volunteers app
│   ├── env/                  # Virtual environment
│   └── manage.py             # Django management script
│
├── frontend/                # React frontend
│   └── better-world-frontend/  # Core frontend project
│
└── README.md                # Project documentation


---

Installation Guide

Prerequisites

1. Node.js (>= 14.x)


2. Python (>= 3.8)


3. PostgreSQL



Step 1: Clone the Repository

git clone https://github.com/allyelvis/make_world_better.git  
cd make_world_better

Step 2: Set Up the Backend

cd backend  
python3 -m venv env  
source env/bin/activate  
pip install -r requirements.txt  
python manage.py migrate  
python manage.py runserver

Step 3: Set Up the Frontend

cd frontend/better-world-frontend  
npm install  
npm start


---

API Endpoints

Initiatives

GET /api/initiatives/: Retrieve a list of all initiatives.


Volunteers

GET /api/volunteers/: Retrieve a list of all volunteers.



---

Demo Data

Sample Initiatives

Sample Volunteers


---

Contributing

We welcome contributions!

1. Fork the repository.


2. Create a new branch.


3. Make your changes and commit them.


4. Push the changes and open a pull request.




---

License

This project is licensed under the MIT License.


---

Acknowledgments

Inspired by the many organizations making a difference worldwide.

Thanks to the open-source community for their amazing tools and support.


Together, we can make the world a better place! 🌟


