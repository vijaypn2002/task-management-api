Task Management API
A simple, role-based Task Management system built with Django and Django REST Framework, using JWT authentication.

This project was developed as part of a machine test assignment.

Features
JWT-based authentication using SimpleJWT
Role-based access: User, Admin, SuperAdmin
Users can view and update their assigned tasks and submit completion reports
Admins can manage tasks and view reports for their assigned users
SuperAdmins can manage users, admins, tasks, and view all reports
Clean API design with Django REST Framework
Enhanced Django admin panel using django-jazzmin
Tech Stack
Backend: Django 5.1.7, Django REST Framework 3.16.0
Authentication: djangorestframework-simplejwt 5.5.0
Admin Interface: django-jazzmin 3.0.1
Database: SQLite (development use)
