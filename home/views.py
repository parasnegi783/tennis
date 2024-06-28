from django.shortcuts import render,redirect
from .models import Participant,card, Event,BankDetail
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404
from datetime import datetime,date
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed
from django.db.models import Q



def calculate_age(date_of_birth):
    if isinstance(date_of_birth, str):
        dob = datetime.strptime(date_of_birth, '%Y-%m-%d').date()
    else:
        dob = date_of_birth
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age


def check_age_requirements(age, partner_age, category):
    if category == 'Open':
        if age > 30 and partner_age > 30:
            return True
    elif category == '90+':
        required_age = 90
    elif category == '105+':
        required_age = 105
    elif category == '120+':
        required_age = 120
    else:
        return False

    if age > 30 and partner_age > 30:
        calculated_age = age + partner_age
        print("Calculated age is", calculated_age)
        if calculated_age >= required_age:
            return True
    
    return False


def home(request):
    cards = card.objects.all()
    return render(request, 'home.html', {'cards': cards})

def edit(request):
    user = request.session.get('username')
    loggedUser = get_object_or_404(Participant, whatsapp_number=user)
    participants = Participant.objects.filter(first_event_partner='Not Registered Yet', second_event_partner='Not Registered Yet').values('name', 'participant_id')
    return render(request, 'edit.html', {'participants': participants,'loggedUser': loggedUser, 'user': user})

def payment(request):
    events = Event.objects.all()
    bank_details = BankDetail.objects.all().first()  
    context = {
        'events': events,
        'bank_details': bank_details,
    }
    return render(request, 'payment.html',context)



def load_participant(request):
    category_name = request.GET.get('category')  

    try:
        participants = Participant.objects.filter(
            Q(second_event_category=category_name) & 
            Q(second_event_partner__in=['Not Registered Yet', 'Not Registered Yet-Not Registered Yet'])
        ).values('name', 'participant_id')
        participants_list = list(participants)  

        return JsonResponse({
            'participants': participants_list
        })

    except Participant.DoesNotExist:
        return JsonResponse({'participants': []})

    except Exception as e:
        print("Error:", str(e))
        return JsonResponse({'error': str(e)}, status=400)

def fetch_participants(request):
    category_name = request.GET.get('category')  

    try:
        participants = Participant.objects.filter(
            Q(first_event_category=category_name) & 
            Q(first_event_partner__in=['Not Registered Yet', 'Not Registered Yet-Not Registered Yet'])
        ).values('name', 'participant_id')

        participants_list = list(participants)  

        return JsonResponse({
            'participants': participants_list
        })

    except Participant.DoesNotExist:
        return JsonResponse({'participants': []})

    except Exception as e:
        print("Error:", str(e))
        return JsonResponse({'error': str(e)}, status=400)

def load_participants(request):
    category_name = request.GET.get('category')  

    try:
        participants = Participant.objects.filter(
            Q(second_event_category=category_name) & 
            Q(second_event_partner__in=['Not Registered Yet', 'Not Registered Yet-Not Registered Yet'])
        ).values('name', 'participant_id')

        logged_in_participant = request.user.username
        logged_in_participant_obj = Participant.objects.filter(whatsapp_number=logged_in_participant).first()

        if logged_in_participant_obj:
            logged_in_participant_id = logged_in_participant_obj.participant_id
            logged_in_second_event_partner = logged_in_participant_obj.second_event_partner
            logged_in_second_event_partner_id = logged_in_participant_obj.second_event_id
        else:
            logged_in_participant_id = None
            logged_in_second_event_partner = None

        print(logged_in_second_event_partner)
        participants_list = list(participants)  

        participants_list = [participant for participant in participants_list if participant['participant_id'] != logged_in_participant_id]

        return JsonResponse({
            'participants': participants_list,
            'logged_in_second_event_partner': logged_in_second_event_partner,
            'logged_in_second_event_partner_id':logged_in_second_event_partner_id
        })

    except Participant.DoesNotExist:
        return JsonResponse({'participants': []})

    except Exception as e:
        print("Error:", str(e))
        return JsonResponse({'error': str(e)}, status=400)

def fetch_participantss(request):
    category_name = request.GET.get('category')  

    try:
        participants = Participant.objects.filter(
            Q(first_event_category=category_name) & 
            Q(first_event_partner__in=['Not Registered Yet', 'Not Registered Yet-Not Registered Yet'])
        ).values('name', 'participant_id')

        logged_in_participant = request.user.username
        logged_in_participant_obj = Participant.objects.filter(whatsapp_number=logged_in_participant).first()

        if logged_in_participant_obj:
            logged_in_participant_id = logged_in_participant_obj.participant_id
            logged_in_first_event_partner = logged_in_participant_obj.first_event_partner
            logged_in_first_event_partner_id = logged_in_participant_obj.first_event_id
        else:
            logged_in_participant_id = None
            logged_in_first_event_partner = None


        participants_list = list(participants)  

        participants_list = [participant for participant in participants_list if participant['participant_id'] != logged_in_participant_id]

        return JsonResponse({
            'participants': participants_list,
            'logged_in_first_event_partner': logged_in_first_event_partner,
            'logged_in_first_event_partner_id': logged_in_first_event_partner_id
        })

    except Participant.DoesNotExist:
        return JsonResponse({'participants': []})

    except Exception as e:
        print("Error:", str(e))
        return JsonResponse({'error': str(e)}, status=400)



def register(request):
    participants = Participant.objects.all()  

    context = {
        'participants': participants,
        'loggedUser': request.user if request.user.is_authenticated else None
    }
    return render(request, 'form.html', context)

@login_required
def detail(request,user=None):
    if request.user.is_authenticated:
        user = request.session.get('username')
        loggedUser = get_object_or_404(Participant, whatsapp_number=user)
        participants = Participant.objects.filter(first_event_partner='Not Registered Yet', second_event_partner='Not Registered Yet').values('name', 'participant_id')
        return render(request, 'form1.html', {'participants': participants,'loggedUser': loggedUser, 'user': user})
    else:
        return render(request, 'login.html')


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('detail')
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    request.session.clear()
    return redirect("home")

def logged_user(request):
    if request.method == 'POST':
        username = request.POST.get('whatsapp_number')
        password = request.POST.get('date_of_birth')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username'] = username 
            return redirect('detail')
        else:
            messages.error(request, 'Invalid WhatsApp number or date of birth.')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')



def update_event_partners(participant):
    parti_name = participant.name
    event_id = participant.participant_id
    first_event_category_name = participant.first_event_category
    second_event_category_name = participant.second_event_category
    first_event_name = participant.first_event_partner
    first_event_id = participant.first_event_id
    if first_event_name != "Not Registered Yet" and first_event_id != "Not Registered Yet":
        try:
            first_event_partner = Participant.objects.get(name=first_event_name, participant_id=first_event_id)
            first_event_partner.first_event_id = participant.participant_id
            first_event_partner.first_event_partner = participant.name
            first_event_partner.save()
        except Participant.DoesNotExist:
            print(f"Participant with name '{first_event_name}' and ID '{first_event_id}' does not exist.")
        except Participant.MultipleObjectsReturned:
            print(f"Multiple participants found with name '{first_event_name}' and ID '{first_event_id}'. Update failed.")

    
    second_event_name = participant.second_event_partner
    second_event_id = participant.second_event_id
    if second_event_name != "Not Registered Yet" and second_event_id != "Not Registered Yet":
        try:
            second_event_partner = Participant.objects.get(name=second_event_name, participant_id=second_event_id)
            second_event_partner.second_event_id = participant.participant_id
            second_event_partner.second_event_partner = participant.name
            second_event_partner.save()
        except Participant.DoesNotExist:
            print(f"Participant with name '{second_event_name}' and ID '{second_event_id}' does not exist.")
        except Participant.MultipleObjectsReturned:
            print(f"Multiple participants found with name '{second_event_name}' and ID '{second_event_id}'. Update failed.")


def save_participant(request):
    if request.method == 'POST':
        print("POST data:", request.POST)
        
        name = request.POST.get('name')
        date_of_birth = request.POST.get('date_of_birth')
        user_age = calculate_age(date_of_birth)
        if user_age<30:
            messages.error(request, "Your age do not meet the requirements.")
            return redirect('register')
        whatsapp_number = request.POST.get('whatsapp_number')
        city = request.POST.get('city')
        email = request.POST.get('email')
        indian_tree_tshirt_size = request.POST.get('indian_tree_tshirt_size')
        indian_tree_shorts_size = request.POST.get('indian_tree_shorts_size')
        food_preference = request.POST.get('food_preference')
        stay_arrangement = request.POST.get('stay_arrangement')
        first_event_name = request.POST.get('first_event')


        if first_event_name != "Not Registered Yet":
            try:
                x, _, y = first_event_name.partition('-')
                first_event_name = x.strip()
                first_event_id = y.strip()
            except ValueError as e:
                print("Error unpacking first event name:", e)
                pass
        else:
            first_event_name = 'Not Registered Yet'
            first_event_id = 'Not Registered Yet'

        second_event_name = request.POST.get('second_event')
        if second_event_name != "Not Registered Yet":
            try:
                a, _, b = second_event_name.partition('-')
                second_event_name = a.strip()
                second_event_id = b.strip()
            except ValueError as e:
                print("Error unpacking second event name:", e)
                pass
        else:
            second_event_name = 'Not Registered Yet'
            second_event_id = 'Not Registered Yet'

        first_event_category = request.POST.get('first_event_category')
        second_event_category = request.POST.get('second_event_category')
        
        if first_event_name != 'Not Registered Yet':
            try:
                first_event_partner_detail = Participant.objects.get(name=first_event_name, participant_id=first_event_id)
                first_event_partner_age = calculate_age(first_event_partner_detail.date_of_birth)
                if not check_age_requirements(user_age, first_event_partner_age, first_event_category):
                    messages.error(request, "Your and First Event Partner age do not meet the requirements.")
                    return redirect('register')
            except Participant.DoesNotExist:
                messages.error(request, "First event partner does not exist.")
                return redirect('register')

        if second_event_name != 'Not Registered Yet':
            try:
                second_event_partner_detail = Participant.objects.get(name=second_event_name, participant_id=second_event_id)
                second_event_partner_age = calculate_age(second_event_partner_detail.date_of_birth)
                if not check_age_requirements(user_age, second_event_partner_age, second_event_category):
                    messages.error(request, "Your and Second Event Partner age do not meet the requirements.")
                    return redirect('register')
            except Participant.DoesNotExist:
                messages.error(request, "Second event partner does not exist.")
                return redirect('register')

        username = request.POST.get('whatsapp_number')
        password = request.POST.get('date_of_birth')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Number already exists. Please choose a different one.')
            return redirect('register')

        try:
            myuser = User.objects.create_user(username=username, password=password)
            myuser.save()
        except Exception as e:
            print("Failed to create custom user:", e)
            return redirect('register')

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
            first_event_partner=first_event_name,
            first_event_category=first_event_category,
            first_event_id=first_event_id,
            second_event_partner=second_event_name,
            second_event_category=second_event_category,
            second_event_id=second_event_id,
        )
  
        try:
            new_participant.save()
            update_event_partners(new_participant)
            messages.success(request, 'Participant saved successfully.')
            return redirect('payment')
        except ObjectDoesNotExist:
            print("Error: Participant data not found.")
            messages.error(request, 'Error: Participant data not found.')
            return redirect('register')
        except Exception as e:
            print("Failed to save participant:", e)
            messages.error(request, 'Failed to save participant.')
            return redirect('register')
    else:
        print("Invalid request method:", request.method)
        return HttpResponse("Method not allowed", status=405)
    
def uuupdate_event_partners_to_not_registered_ist(first_event_partner_for_update,first_event_id_for_update):
    first_event_name=first_event_partner_for_update
    first_event_id=first_event_id_for_update
    try:
        first_event_partners = Participant.objects.get(name=first_event_name, participant_id=first_event_id)
        print("first_event_partners",first_event_partners)
        first_event_partners.first_event_id = "Not Registered Yet"
        first_event_partners.first_event_partner = "Not Registered Yet"
        print("first_event_partners.first_event_id",first_event_partners.first_event_id)
        first_event_partners.save()
    except (Participant.DoesNotExist, Participant.MultipleObjectsReturned) as e:
        print("Error updating first event partner:", e)

def uuupdate_event_partners_to_not_registered_scnd(second_event_partner_for_update,second_event_id_for_update):
    second_event_name=second_event_partner_for_update
    second_event_id=second_event_id_for_update
    try:
        second_event_partners = Participant.objects.get(name=second_event_name, participant_id=second_event_id)
        print("second_event_partners",second_event_partners)
        second_event_partners.second_event_id = "Not Registered Yet"
        second_event_partners.second_event_partner = "Not Registered Yet"
        second_event_partners.save()
    except (Participant.DoesNotExist, Participant.MultipleObjectsReturned) as e:
        print("Error updating second event partner:", e)


def uuupdate_event_partners_ist(participant):
    first_event_name = participant.first_event_partner
    first_event_id = participant.first_event_id
    if first_event_name != "Not Registered Yet" and first_event_name != "Not Registered Yet-Not Registered Yet" and first_event_id != "Not Registered Yet" and first_event_id != "Not Registered Yet-Not Registered Yet":
        try:
            first_event_partners = Participant.objects.get(name=first_event_name, participant_id=first_event_id)
            first_event_partners.first_event_id = participant.participant_id
            first_event_partners.first_event_partner = participant.name
            print("first_event_partners.first_event_id",first_event_partners.first_event_id)
            first_event_partners.save()
        except (Participant.DoesNotExist, Participant.MultipleObjectsReturned) as e:
            print("Error updating first event partner:", e)

def uuupdate_event_partners_scnd(participant):       
    second_event_name = participant.second_event_partner
    second_event_id = participant.second_event_id
    if second_event_name != "Not Registered Yet" and second_event_name != "Not Registered Yet-Not Registered Yet" and second_event_id != "Not Registered Yet" and second_event_id != "Not Registered Yet-Not Registered Yet":  
        try:
            second_event_partners = Participant.objects.get(name=second_event_name, participant_id=second_event_id)
            second_event_partners.second_event_id = participant.participant_id
            second_event_partners.second_event_partner = participant.name
            second_event_partners.save()
        except (Participant.DoesNotExist, Participant.MultipleObjectsReturned) as e:
            print("Error updating second event partner:", e)
    

import logging

from datetime import datetime

logger = logging.getLogger(__name__)

def update_save_participant(request):
    logger.info("Entering update_save_participant")

    if request.method == 'POST':
        user = request.session.get('username')
        loggedUser = get_object_or_404(Participant, whatsapp_number=user)

        name = request.POST.get('name')
        date_of_birth = request.POST.get('date_of_birth')
        user_age = calculate_age(date_of_birth)
        print("User age:", user_age)
        if user_age<30:
                messages.error(request, "Your and First Event Partner age do not meet the requirements.")
                return redirect('edit')
        whatsapp_number = request.POST.get('whatsapp_number')
        city = request.POST.get('city')
        email = request.POST.get('email')
        indian_tree_tshirt_size = request.POST.get('indian_tree_tshirt_size')
        indian_tree_shorts_size = request.POST.get('indian_tree_shorts_size')
        food_preference = request.POST.get('food_preference')
        stay_arrangement = request.POST.get('stay_arrangement')
        first_event_name = request.POST.get('first_event')
        first_event_category = request.POST.get('first_event_category')
        second_event_name = request.POST.get('second_event')
        second_event_category = request.POST.get('second_event_category')

        # Process first event name and ID
        if first_event_name != "Not Registered Yet":
            try:
                a, _, b = first_event_name.partition('-')
                first_event_name = a.strip()
                first_event_id = b.strip()
            except ValueError as e:
                print("Error unpacking first event name:", e)
                pass
        else:
            first_event_name = 'Not Registered Yet'
            first_event_id = 'Not Registered Yet'

        # Process second event name and ID
        if second_event_name != "Not Registered Yet":
            try:
                a, _, b = second_event_name.partition('-')
                second_event_name = a.strip()
                second_event_id = b.strip()
            except ValueError as e:
                print("Error unpacking first event name:", e)
                pass
        else:
            second_event_name = 'Not Registered Yet'
            second_event_id = 'Not Registered Yet'


        # Validate first event partner's age
        if first_event_name != 'Not Registered Yet':
            first_event_partner_detail = get_object_or_404(Participant, name=first_event_name, participant_id=first_event_id)
            first_event_partner_age = calculate_age(first_event_partner_detail.date_of_birth)
            print("first_event_partner_age",first_event_partner_age)
            if not check_age_requirements(user_age, first_event_partner_age, first_event_category):
                messages.error(request, "Your and First Event Partner age do not meet the requirements.")
                return redirect('edit')
            first_event_id = first_event_partner_detail.participant_id

        # Validate second event partner's age
        if second_event_name != 'Not Registered Yet':
            try:
                second_event_partner_detail = Participant.objects.get(name=second_event_name, participant_id=second_event_id)
            except Participant.DoesNotExist:
                messages.error(request, "Participant with the specified details not found.")
                return redirect('edit')
            second_event_partner_age = calculate_age(second_event_partner_detail.date_of_birth)
            print("second_event_partner_age",second_event_partner_age)
            if not check_age_requirements(user_age, second_event_partner_age, second_event_category):
                messages.error(request, "Your and Second Event Partner age do not meet the requirements.")
                return redirect('edit')
            second_event_id = second_event_partner_detail.participant_id

        old_whatsapp_number = loggedUser.whatsapp_number
        old_DateOfBirth = loggedUser.date_of_birth.strftime('%Y-%m-%d')
        first_event_id_for_update=loggedUser.first_event_id
        first_event_partner_for_update=loggedUser.first_event_partner
        if first_event_id_for_update!="Not Registered Yet" and first_event_id_for_update!="Not Registered Yet-Not Registered Yet":
            uuupdate_event_partners_to_not_registered_ist(first_event_partner_for_update,first_event_id_for_update)
        second_event_id_for_update=loggedUser.second_event_id
        second_event_partner_for_update=loggedUser.second_event_partner
        if second_event_id_for_update!="Not Registered Yet" and second_event_id_for_update!="Not Registered Yet-Not Registered Yet":
            uuupdate_event_partners_to_not_registered_scnd(second_event_partner_for_update,second_event_id_for_update)
        # Update logged user's information
        loggedUser.name = name
        loggedUser.date_of_birth = date_of_birth
        loggedUser.city = city
        loggedUser.email = email
        loggedUser.indian_tree_tshirt_size = indian_tree_tshirt_size
        loggedUser.indian_tree_shorts_size = indian_tree_shorts_size
        loggedUser.food_preference = food_preference
        loggedUser.stay_arrangement = stay_arrangement
        loggedUser.first_event_partner = first_event_name
        loggedUser.first_event_category = first_event_category
        loggedUser.first_event_id = first_event_id
        loggedUser.second_event_partner = second_event_name
        loggedUser.second_event_category = second_event_category
        loggedUser.second_event_id = second_event_id
        loggedUser.whatsapp_number = whatsapp_number

        new_DateOfBirth = date_of_birth.strftime('%Y-%m-%d') if isinstance(date_of_birth, datetime) else date_of_birth

        loggedUser.save()
        if first_event_id_for_update=="Not Registered Yet" or first_event_id_for_update=="Not Registered Yet-Not Registered Yet":
            uuupdate_event_partners_ist(loggedUser)
        elif second_event_id_for_update=="Not Registered Yet" or second_event_id_for_update=="Not Registered Yet-Not Registered Yet":
            uuupdate_event_partners_scnd(loggedUser)
        
        try:
            
            user_object = User.objects.get(username=user)

            if old_whatsapp_number != whatsapp_number or old_DateOfBirth != new_DateOfBirth:
                user_object.username = whatsapp_number
                user_object.set_password(new_DateOfBirth) 
                user_object.save()

                if old_whatsapp_number != whatsapp_number and old_DateOfBirth != new_DateOfBirth:
                    messages.success(request, 'Participant information updated successfully. Please log in again with your new WhatsApp number and password.')
                    return redirect('login')
                elif old_whatsapp_number != whatsapp_number:
                    messages.success(request, 'Participant information updated successfully. Please log in again with your new WhatsApp number.')
                    return redirect('login')
                elif old_DateOfBirth != new_DateOfBirth:
                    messages.success(request, 'Participant information updated successfully. Please log in again with your new password.')
                    return redirect('login')
                else:
                    messages.success(request, 'Participant information updated successfully.')
                    return redirect('detail')
            else:
                messages.success(request, 'Participant information updated successfully.')
                return redirect('detail')
        except Exception as e:
            print("Are you searching for me",e)
            messages.error(request, 'Failed to update participant information.')
            return redirect('edit')
    else:
        return HttpResponseNotAllowed(['POST'])
