# validators.py
from django.core.exceptions import ValidationError

def validate_com(value):
    if not value.endswith('.com'):
        raise ValidationError('Email address must end with .com')
