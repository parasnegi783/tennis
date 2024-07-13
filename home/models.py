from django.db import models

class card(models.Model):
    heading=models.CharField(max_length=40,null=True, default=None)
    point1=models.CharField(max_length=220,null=True,blank=True)
    point2=models.CharField(max_length=220,null=True,blank=True)
    point3=models.CharField(max_length=220,null=True,blank=True)
    point4=models.CharField(max_length=220,null=True,blank=True)
    point5=models.CharField(max_length=220,null=True,blank=True)

    def __str__(self):
        return str(self.heading)


class Participant(models.Model):
    participant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=True, default=None)
    whatsapp_number = models.CharField(max_length=15,null=True, default=None, unique=True)
    date_of_birth = models.DateField(null=True, default=None)
    city = models.CharField(max_length=100,null=True, default=None)
    first_event_category = models.CharField(max_length=20,null=True, default=None)
    first_event_partner = models.CharField(max_length=20,null=True, default=None)
    first_event_id = models.CharField(max_length=20,null=True, default=None)
    second_event_category = models.CharField(max_length=20,null=True, default=None)
    second_event_partner = models.CharField(max_length=20,null=True, default=None)
    second_event_id = models.CharField(max_length=20,null=True, default=None)
    indian_tree_tshirt_size = models.CharField(max_length=20,null=True, default=None)
    indian_tree_shorts_size = models.CharField(max_length=20,null=True, default=None)
    food_preference = models.CharField(max_length=20,null=True, default=None)
    email = models.EmailField(null=True, default=None) 
    stay_arrangement = models.CharField(max_length=3,null=True, default=None)

    def __str__(self):
        return str(self.name)

class category(models.Model):
    Event_category = models.CharField(max_length=100)
    def __str__(self):
        return str(self.Event_category)

class TeamForFirstEvent(models.Model):
    team_id = models.AutoField(primary_key=True)
    first_partner = models.ForeignKey(Participant, related_name='first_event_first_partner', on_delete=models.CASCADE)
    second_partner = models.ForeignKey(Participant, related_name='first_event_second_partner', on_delete=models.CASCADE)
    event = models.ForeignKey(category, related_name='first_event_teams', on_delete=models.CASCADE,blank=True,default=None)

    def __str__(self):
        return f"Team ID: {self.team_id}, First Partner: {self.first_partner.name}, Second Partner: {self.second_partner.name}, Event: {self.event.Event_category}"


class TeamForSecondEvent(models.Model):
    team_id = models.AutoField(primary_key=True)
    first_partner = models.ForeignKey(Participant, related_name='second_event_first_partner', on_delete=models.CASCADE)
    second_partner = models.ForeignKey(Participant, related_name='second_event_second_partner', on_delete=models.CASCADE)
    event = models.ForeignKey(category, related_name='second_event_teams', on_delete=models.CASCADE,blank=True,default=None)

    def __str__(self):
        return f"Team ID: {self.team_id}, First Partner: {self.first_partner.name}, Second Partner: {self.second_partner.name}, Event: {self.event.Event_category}"

    

class BankDetail(models.Model):
    account_number = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    qr_code_image = models.ImageField(upload_to='qr_codes/')

    def __str__(self):
        return f'{self.bank_name} ({self.branch_name})'

class Event(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
class PaymentInfo(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    additional_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    bank_detail = models.ForeignKey(BankDetail, on_delete=models.CASCADE)

    def __str__(self):
        return f'Payment Info for {self.event.name}'

