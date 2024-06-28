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

# from django import forms
# from .models import FirstEventCategory, FirstEventName

# class FirstEventNameForm(forms.Form):
#     category = forms.ModelChoiceField(queryset=FirstEventCategory.objects.all(),
#         widget=forms.Select(attrs={"hx-get": "load_event_names/", "hx-target": "#id_event_name"}))
#     event_name = forms.ModelChoiceField(queryset=FirstEventName.objects.none())

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if "category" in self.data:
#             try:
#                 category_id = int(self.data.get("category"))
#                 self.fields["event_name"].queryset = FirstEventName.objects.filter(category_id=category_id)
#             except (ValueError, TypeError):
#                 self.fields["event_name"].queryset = FirstEventName.objects.none()
from django import forms
