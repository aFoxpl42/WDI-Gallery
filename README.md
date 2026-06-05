# WIT Animacje 3D - Student Gallery Web App

A responsive, Django-based Web application designed for university instructors to showcase and manage student animations, VFX projects, and 3D models.

## Features
* Custom Teacher Dashboard: Secure, authenticated portal for instructors to Add, Edit, and Delete student artworks.
* Role-Based Authorization: Backend security ensures instructors can only modify artworks they personally uploaded.
* Dual-Media Support: Handles both local .mp4 video uploads and dynamic YouTube iframe embeds.
* Dynamic Grouping: Artworks are automatically queried and grouped on the frontend by Academic Year and Semester, sorted chronologically.
* Responsive UI: Fully responsive frontend built natively with CSS Flexbox and Grid.

## Tech Stack
* Backend: Python, Django
* Database: SQLite (Development)
* Frontend: HTML5, CSS3
* Media Handling: Pillow

## Local Setup

1. Clone the repository:
   git clone https://github.com/aFoxpl42/WDI-Gallery.git
   cd WDI-Gallery

2. Create and activate a virtual environment:
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Apply database migrations:
   python manage.py migrate

5. Create a superuser:
   python manage.py createsuperuser

6. Run the development server:
   python manage.py runserver