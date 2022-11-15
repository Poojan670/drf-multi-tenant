from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=100, unique=True)
    schema_name = models.CharField(max_length=100, unique=True)
    sub_domain = models.CharField(max_length=300, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} : {self.sub_domain}"
