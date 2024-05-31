from django.shortcuts import render,redirect
from .models import Participant,card
from django.http import HttpResponseRedirect
from django.core.exceptions import MultipleObjectsReturned
from django.contrib import messages
from django.urls import reverse

import random

def home(request):
    cards = card.objects.all()
    return render(request, 'home.html', {'cards': cards})

def register(request):
    participants = Participant.objects.filter(first_event='Not Registered', second_event='Not Registered').values('name', 'participant_id')
    return render(request, 'form1.html', {'participants': participants})

def login(request):
    if request.method == 'POST':
        whatsapp_number = request.POST.get('whatsapp_number')
        date_of_birth = request.POST.get('date_of_birth')
        try:
            participant = Participant.objects.get(whatsapp_number=whatsapp_number, date_of_birth=date_of_birth)
            return render(request, 'form1.html', {'participant': participant})
        except Participant.DoesNotExist:
            messages.error(request, 'Invalid WhatsApp number or date of birth.')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def save_participant(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        date_of_birth = request.POST.get('date_of_birth')
        whatsapp_number = request.POST.get('whatsapp_number')
        city = request.POST.get('city')
        email = request.POST.get('email')
        indian_tree_tshirt_size = request.POST.get('indian_tree_tshirt-size')
        indian_tree_shorts_size = request.POST.get('indian_tree_shorts-size')
        food_preference = request.POST.get('food_preference')
        stay_arrangement = request.POST.get('stay_arrangement')
        first_event_name = request.POST.get('first_event')

        if first_event_name != "Not Registered":
            try:
                first_event_partner = Participant.objects.get(name=first_event_name)
                first_event_partner.first_event = name 
                first_event_partner.save()
            except Participant.DoesNotExist:
                print("Participant for the first event was not found.")
            except MultipleObjectsReturned:
                first_event_partner = Participant.objects.filter(name=first_event_name).first()
                first_event_partner.first_event = name 
                first_event_partner.save()

        second_event_name = request.POST.get('second_event')
        if second_event_name != "Not Registered":
            try:
                second_event_partner = Participant.objects.get(name=second_event_name)
                second_event_partner.second_event = name 
                second_event_partner.save()
            except Participant.DoesNotExist:
                print("Participant for the second event was not found.")
            except Participant.MultipleObjectsReturned:
                second_event_partner = Participant.objects.filter(name=second_event_name).first()
                second_event_partner.second_event = name 
                second_event_partner.save()

        new_participant = Participant(
            name=name,
            date_of_birth=date_of_birth,
            whatsapp_number=whatsapp_number,
            city=city,
            email=email,
            indian_tree_tshirt_size=indian_tree_tshirt_size,
            indian_tree_shorts_size=indian_tree_shorts_size,
            food_preference=food_preference,
            stay_arrangement=stay_arrangement,
            first_event=first_event_name,
            second_event=second_event_name,
        )
        try:
            new_participant.save()
            print("Participant ID:", new_participant.participant_id)
        except Exception as e:
            print(e)
        else:
            print("hello")
            messages.success(request, 'Participant saved successfully.')
            return redirect('home')
