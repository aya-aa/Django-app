from django.contrib.auth.models import Permission

view_recruiter_interface = Permission.objects.create(
    codename='view_recruiter_interface',
    name='Can view recruiter interface'
)
