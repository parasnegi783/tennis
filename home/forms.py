from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models



class CustomUserManager(UserManager):
    def create_user(self, whatsapp_number, date_of_birth, **extra_fields):
        extra_fields.setdefault('username', whatsapp_number)
        user = self.model(**extra_fields)
        user.set_password(date_of_birth)
        user.save(using=self._db)
        return user

class CreateUser(AbstractUser):
    whatsapp_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()

    objects = CustomUserManager()

    def __str__(self):
        return self.username  # You can change this to whatsapp_number or any other field you prefer


from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = [
            'name', 'date_of_birth', 'whatsapp_number', 'city', 'email',
            'indian_tree_tshirt_size', 'indian_tree_shorts_size', 'food_preference',
            'stay_arrangement', 'first_event_category', 'first_event_partner',
            'first_event_id', 'second_event_category', 'second_event_partner', 'second_event_id'
        ]