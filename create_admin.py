"""
Run this script once to create the admin account.
Usage:  python create_admin.py
"""
import os
import django
import hashlib
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'plagiarism_detector.settings')
django.setup()

from core.db import db

email = 'admin@sece.ac.in'
password = 'admin123'

if db.users.find_one({'email': email}):
    print(f"Admin '{email}' already exists.")
else:
    db.users.insert_one({
        'name': 'Admin',
        'email': email,
        'password': hashlib.sha256(password.encode()).hexdigest(),
        'role': 'admin',
        'created_at': datetime.now(),
    })
    print("✅ Admin account created!")
    print(f"   Email:    {email}")
    print(f"   Password: {password}")
    print("\nRun:  python manage.py runserver")
