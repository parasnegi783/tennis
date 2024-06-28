from django.contrib import admin
from .models import Participant,card,Event,BankDetail,PaymentInfo

admin.site.register(Participant)
admin.site.register(card)

admin.site.register(Event)
admin.site.register(BankDetail)
admin.site.register(PaymentInfo)

