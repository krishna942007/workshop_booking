from django.contrib.auth.models import User
from workshop_app.models import Profile, Workshop, WorkshopType
import datetime

def fix():
    admin = User.objects.get(username='admin')
    
    # Ensure profile exists with correct state
    p, created = Profile.objects.get_or_create(
        user=admin,
        defaults={
            'institute': 'IIT Bombay',
            'department': 'electronics',
            'phone_number': '9999999999',
            'position': 'instructor',
            'state': 'IN-MH',
            'is_email_verified': True
        }
    )
    if not created:
        p.state = 'IN-MH'
        p.is_email_verified = True
        p.save()
    
    # Ensure workshop exists with status=1
    wt, _ = WorkshopType.objects.get_or_create(
        name='Basics of Python',
        defaults={'description': 'Intro', 'duration': 1}
    )
    
    Workshop.objects.update_or_create(
        coordinator=admin,
        workshop_type=wt,
        date=datetime.date.today(),
        defaults={'status': 1, 'tnc_accepted': True}
    )
    
    print("Fix applied: Admin profile and workshop data normalized.")

if __name__ == '__main__':
    fix()
