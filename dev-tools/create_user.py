from django.contrib.auth.models import User # pylint: disable=imported-auth-user

user="lunes"
email="admin@lunes.app"
password="lunes"

if user not in User.objects.values_list("username", flat=True):
    User.objects.create_superuser(user, email, password)