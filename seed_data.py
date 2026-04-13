import os
import django
import sys

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workshop_portal.settings')
django.setup()

from django.contrib.auth.models import User
from workshop_app.models import Profile, Workshop, WorkshopType
import datetime

def fix_data():
    print("--- Seeding Data for Statistics Page ---")
    
    # 1. Get or create Superuser
    user, created = User.objects.get_or_create(username='admin')
    if created:
        user.set_password('admin123')
        user.is_superuser = True
        user.is_staff = True
        user.save()
        print(f"Created user: {user.username}")

    # 2. Get or create Profile (crucial for stats page)
    profile, created = Profile.objects.get_or_create(user=user)
    if created or not profile.institute:
        profile.institute = "Indian Institute of Technology"
        profile.state = "Maharashtra"
        profile.save()
        print(f"Updated profile for {user.username}")

    # 3. Get or create Workshop Type
    wtype, created = WorkshopType.objects.get_or_create(
        name="Python for Data Science",
        defaults={
            'duration': 5, 
            'description': "A comprehensive course on Python for Data Science.",
            'terms_and_conditions': "Standard terms apply."
        }
    )
    if created:
        print(f"Created Workshop Type: {wtype.name}")

    # 4. Create a Workshop if none exist
    if Workshop.objects.count() == 0:
        workshop = Workshop.objects.create(
            coordinator=user,
            workshop_type=wtype,
            date=datetime.date.today(),
            status=1, # Success
            is_public=True
        )
        print(f"Created sample workshop: {workshop}")
    else:
        print(f"Found {Workshop.objects.count()} workshops.")

    print("--- Seeding Complete ---")

if __name__ == "__main__":
    fix_data()
