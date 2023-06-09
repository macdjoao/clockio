from django.db import models


class User(models.Model):
    email = models.EmailField(null=False, blank=False, unique=True)
    password = models.CharField(null=False, blank=False)
    first_name = models.CharField(null=False, blank=False)
    last_name = models.CharField(null=False, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'\nemail: {self.email}\nfirst_name: {self.first_name}\nlast_name: {self.last_name}\nis_active: {self.is_active}'
