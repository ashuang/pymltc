import django.contrib.auth.models
from django.db import models

class AuthLog(models.Model):
    id = models.IntegerField(primary_key=True)
    timestamp = models.DateTimeField()
    source = models.CharField(max_length=30)
    user = models.ForeignKey(django.contrib.auth.models.User)
    message = models.CharField(max_length=255)

    class Meta:
        db_table = 'auth_log'
        ordering = ('-timestamp',)
