from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from accounts.models import CustomUser as User
def validate_username(value):
    if len(value) < 4:
        raise ValidationError(_('Le nom d\'utilisateur doit comporter au moins 4 caractères.'), code='invalid')
    elif User.objects.filter(username=value).exists():
        raise ValidationError(_('Ce nom d\'utilisateur est déjà utilisé. Veuillez en choisir un autre.'), code='invalid')

def validate_first_name(value):
    if len(value) < 4:
        raise ValidationError(_('Le nom doit comporter au moins 4 caractères.'), code='invalid')

def validate_last_name(value):
    if len(value) < 4:
        raise ValidationError(_('Le prénom doit comporter au moins 4 caractères.'), code='invalid')

def validate_contact(value):
    
    if User.objects.filter(contact=value).exists():
        raise ValidationError(_('Le numéro de téléphone à déja été utilisé.'), code='invalid')
    
def mail_is_unique(value):
    if User.objects.filter(email=value).exists():
        raise ValidationError(_('Cette adresse mail est déjà utilisé. Veuillez en choisir un autre.'), code='invalid')
    

def validate_password(password):
  # Check if the password is at least 8 characters long.
  if len(password) < 8:
    return False
  # Check if the password contains at least one capital letter.
  if not any(char.isupper() for char in password):
    return False
  # Check if the password contains at least one number.
  if not any(char.isdigit() for char in password):
    return False
  # The password meets all the criteria.
  return True




