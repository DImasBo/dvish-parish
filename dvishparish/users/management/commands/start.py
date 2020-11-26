from django.core.management.base import BaseCommand, CommandError
from rolepermissions.roles import assign_role
from dvishparish.users.models import User


class Command(BaseCommand):
    help = "set start settings"

    def handle(self, *args, **options):
        user_name_list = ["manager", "finance", 'hr', "businesses"]
        for user_name in user_name_list:
            user = User.objects.get_or_create(username=user_name, password="test")
            assign_role(user, user_name)