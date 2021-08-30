from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class URLAlias(models.Model):
    id = models.BigAutoField(primary_key=True)
    alias = models.TextField(unique=True, null=False)
    fullurl = models.TextField(null=False)
    created_at = models.DateTimeField(default=timezone.now)


