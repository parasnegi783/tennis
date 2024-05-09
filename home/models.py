from django.db import models

class card(models.Model):
    heading=models.CharField(max_length=40,null=True, default=None)
    point1=models.CharField(max_length=220,null=True,blank=True)
    point2=models.CharField(max_length=220,null=True,blank=True)
    point3=models.CharField(max_length=220,null=True,blank=True)
    point4=models.CharField(max_length=220,null=True,blank=True)
    point5=models.CharField(max_length=220,null=True,blank=True)

    def __str__(self):
        return self.heading



class FirstEvent(models.Model):
    first_event_choice = models.CharField(max_length=120,null=True, default=None)
    first_event_partner = models.CharField(max_length=100,null=True, default=None)
    p1_indian_tree_tshirt_size = models.CharField(max_length=20,null=True, default=None)
    p1_indian_tree_shorts_size = models.CharField(max_length=20,null=True, default=None)
    p1_food_preference = models.CharField(max_length=20,null=True, default=None)
    p1_stay_arrangement = models.CharField(max_length=3,null=True, default=None)

    def __str__(self):
        return self.first_event_choice

class SecondEvent(models.Model):
    second_event_choice = models.CharField(max_length=120,null=True, default=None)
    second_event_partner = models.CharField(max_length=100,null=True, default=None)
    p2_indian_tree_tshirts_size = models.CharField(max_length=20,null=True, default=None)
    p2_indian_tree_shorts_size = models.CharField(max_length=20,null=True, default=None)
    p2_food_preference = models.CharField(max_length=20,null=True, default=None)
    p2_stay_arrangement = models.CharField(max_length=3,null=True, default=None)

    def __str__(self):
        return self.second_event_choice

class Participant(models.Model):
    participant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=True, default=None)
    whatsapp_number = models.CharField(max_length=15,null=True, default=None)
    date_of_birth = models.DateField(null=True, default=None)
    city = models.CharField(max_length=100,null=True, default=None)
    first_event = models.ForeignKey(FirstEvent, on_delete=models.CASCADE,null=True,default=None)
    second_event = models.ForeignKey(SecondEvent, on_delete=models.CASCADE,null=True,default=None)
    indian_tree_tshirt_size = models.CharField(max_length=20,null=True, default=None)
    indian_tree_shorts_size = models.CharField(max_length=20,null=True, default=None)
    food_preference = models.CharField(max_length=20,null=True, default=None)
    email = models.EmailField(null=True, default=None) 
    stay_arrangement = models.CharField(max_length=3,null=True, default=None)

    def __int__(self):
        return self.participant_id