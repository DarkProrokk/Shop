from django.core.management.base import BaseCommand
from dotenv import dotenv_values
from User.models import CustomUser as User
config = dotenv_values(".env.dev")


class Command(BaseCommand):

    def handle(self, *args, **options):
        username = config.get('ADMIN_NAME')
        password = config.get('ADMIN_PASS')
        email = config.get("ADMIN_EMAIL")

        if not User.objects.filter(username=username).exists():
            print(f"Creating account for {username} email: {email}")
            User.objects.create_superuser(username=username, email=email, password=password)
        else:
            print('Admin account has already been initialized.')