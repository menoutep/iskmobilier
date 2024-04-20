from django.db import models

from django.contrib.auth.models import User


class TypeUser(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

USER_TYPE_CHOICES = (
    ('visitor','visitor'),
    ('vendor','vendor'),
    ('isk_account','isk_account'),
)  
class CustomUser(User):
    contact = models.CharField(max_length=20)
    type = models.CharField(max_length=200,choices=USER_TYPE_CHOICES,default='visitor')
    # Ajoutez d'autres champs personnalisés si nécessaire
    def __str__(self):
        return self.username
    
