from django.shortcuts import render,redirect
from .models import Participant,card
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404
from datetime import datetime,date
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed

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
        return True
    elif category == '90+':
        required_age = 90
    elif category == '105+':
        required_age = 105
    elif category == '120+':
        required_age = 120
    else:
        return False

    if age > 15 and partner_age > 15:
        calculated_age = age + partner_age
        print("Calculated age is", calculated_age)
        if calculated_age >= required_age:
            return True
    
    return False





def home(request):
    cards = card.objects.all()
    return render(request, 'home.html', {'cards': cards})


def register(request):
    participants = Participant.objects.filter(
        first_event_partner='Not Registered', second_event_partner='Not Registered'
    ).values('name', 'participant_id')
    return render(request, 'form1.html', {'participants': participants})

def detail(request,user=None):
    user = request.session.get('username')
    print("user:",user)
    print("Username:", user)
    loggedUser = get_object_or_404(Participant, whatsapp_number=user)
    print("Logged User:", loggedUser)
    print("First Event Partner:", loggedUser.first_event_partner)
    participants = Participant.objects.filter(first_event_partner='Not Registered', second_event_partner='Not Registered').values('name', 'participant_id')
    return render(request, 'form1.html', {'participants': participants,'loggedUser': loggedUser, 'user': user})


def loginUser(request):
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    request.session.clear()
    return redirect("home")

def logged_user(request):
    if request.method == 'POST':
        print("hello")
        username = request.POST.get('whatsapp_number')
        password = request.POST.get('date_of_birth')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username'] = username 
            return redirect('detail')
        else:
            print("user is invalid")
            messages.error(request, 'Invalid WhatsApp number or date of birth.')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def update_event_partners(participant):
    first_event_name = participant.first_event_partner
    first_event_id = participant.first_event_id
    if first_event_name != "Not Registered" and first_event_id != "Not Registered":
        try:
            first_event_partners = Participant.objects.get(name=first_event_name, participant_id=first_event_id)
            first_event_partners.first_event_id = participant.participant_id
            first_event_partners.first_event_partner = participant.name
            first_event_partners.save()
        except (Participant.DoesNotExist, Participant.MultipleObjectsReturned) as e:
            print("Error updating first event partner:", e)

    second_event_name = participant.second_event_partner
    second_event_id = participant.second_event_id
    if second_event_name != "Not Registered" and first_event_id != "Not Registered":
        try:
            second_event_partners = Participant.objects.get(name=second_event_name, participant_id=second_event_id)
            second_event_partners.second_event_id = participant.participant_id
            second_event_partners.second_event_partner = participant.name
            second_event_partners.save()
        except (Participant.DoesNotExist, Participant.MultipleObjectsReturned) as e:
            print("Error updating second event partner:", e)

def save_participant(request):
    if request.method == 'POST':
        print("POST data:", request.POST)
        
        name = request.POST.get('name')
        date_of_birth = request.POST.get('date_of_birth')
        user_age = calculate_age(date_of_birth)
        print(f"User date of birth: {date_of_birth}, User age: {user_age}")
        
        whatsapp_number = request.POST.get('whatsapp_number')
        city = request.POST.get('city')
        email = request.POST.get('email')
        indian_tree_tshirt_size = request.POST.get('indian_tree_tshirt_size')
        indian_tree_shorts_size = request.POST.get('indian_tree_shorts_size')
        food_preference = request.POST.get('food_preference')
        stay_arrangement = request.POST.get('stay_arrangement')
        first_event_name = request.POST.get('first_event')
        
        
            


        if first_event_name != "Not Registered":
            try:
                x, _, y = first_event_name.partition('-')
                first_event_name = x.strip()
                first_event_id = y.strip()
                print("First event name:", first_event_name, "First event ID:", first_event_id)
            except ValueError as e:
                print("Error unpacking first event name:", e)
                pass
        else:
            first_event_name = 'Not Registered'
            first_event_id = 'Not Registered'
            print("First event not registered")

        second_event_name = request.POST.get('second_event')
        if second_event_name != "Not Registered":
            try:
                a, _, b = second_event_name.partition('-')
                second_event_name = a.strip()
                second_event_id = b.strip()
                print("Second event name:", second_event_name, "Second event ID:", second_event_id)
            except ValueError as e:
                print("Error unpacking second event name:", e)
                pass
        else:
            second_event_name = 'Not Registered'
            second_event_id = 'Not Registered'
            print("Second event not registered")

        first_event_category = request.POST.get('first_event_category')
        second_event_category = request.POST.get('second_event_category')
        if first_event_category != second_event_category:
            messages.error(request, "Both participants must choose the same category for the event.")
            return redirect('register')
        if first_event_name != 'Not Registered':
            try:
                first_event_partner_detail = Participant.objects.get(name=first_event_name, participant_id=first_event_id)
                category1=first_event_partner_detail.first_event_category
                if category1!=first_event_category:
                    messages.error(request, "Participant's category does not match the category of the first event partner.")
                    return redirect('detail')
                first_event_partner_age = calculate_age(first_event_partner_detail.date_of_birth)
                print(f"First event partner date of birth: {first_event_partner_detail.date_of_birth}, First event partner age: {first_event_partner_age}")
                if not check_age_requirements(user_age, first_event_partner_age, first_event_category):
                    messages.error(request, "Your and First Event Partner age do not meet the requirements.")
                    print("First event age requirement not met")
                    return redirect('register')
            except Participant.DoesNotExist:
                print("First event partner does not exist")
                messages.error(request, "First event partner does not exist.")
                return redirect('register')

        if second_event_name != 'Not Registered':
            try:
                second_event_partner_detail = Participant.objects.get(name=second_event_name, participant_id=second_event_id)
                category1=second_event_partner_detail.second_event_category
                if category1!=second_event_category:
                    messages.error(request, "Participant's category does not match the category of the Second event partner.")
                    return redirect('detail')
                second_event_partner_age = calculate_age(second_event_partner_detail.date_of_birth)
                print(f"Second event partner date of birth: {second_event_partner_detail.date_of_birth}, Second event partner age: {second_event_partner_age}")
                if not check_age_requirements(user_age, second_event_partner_age, second_event_category):
                    messages.error(request, "Your and Second Event Partner age do not meet the requirements.")
                    print("Second event age requirement not met")
                    return redirect('register')
            except Participant.DoesNotExist:
                print("Second event partner does not exist")
                messages.error(request, "Second event partner does not exist.")
                return redirect('register')

        username = request.POST.get('whatsapp_number')
        password = request.POST.get('date_of_birth')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Number already exists. Please choose a different one.')
            print("Username already exists:", username)
            return redirect('register')

        try:
            myuser = User.objects.create_user(username=username, password=password)
            myuser.save()
            print("User created:", username)
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
            print("Participant saved with ID:", new_participant.participant_id)
            messages.success(request, 'Participant saved successfully.')
            return redirect('home')
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
    

def uuupdate_event_partners(participant):
    first_event_name = participant.first_event_partner
    first_event_id = participant.first_event_id
    print(first_event_id)
    print(first_event_name)
    if first_event_name != "Not Registered" and first_event_name != "Not Registered-Not Registered" and first_event_id != "Not Registered" and first_event_id != "Not Registered-Not Registered":
        try:
            first_event_partners = Participant.objects.get(name=first_event_name, participant_id=first_event_id)
            first_event_partners.first_event_id = participant.participant_id
            first_event_partners.first_event_partner = participant.name
            first_event_partners.save()
        except (Participant.DoesNotExist, Participant.MultipleObjectsReturned) as e:
            print("Error updating first event partner:", e)

    print("first hurdle clear")
    second_event_name = participant.second_event_partner
    second_event_id = participant.second_event_id
    if second_event_name != "Not Registered" and second_event_name != "Not Registered-Not Registered" and second_event_id != "Not Registered" and second_event_id != "Not Registered-Not Registered":  
        try:
            second_event_partners = Participant.objects.get(name=second_event_name, participant_id=second_event_id)
            second_event_partners.second_event_id = participant.participant_id
            second_event_partners.second_event_partner = participant.name
            second_event_partners.save()
        except (Participant.DoesNotExist, Participant.MultipleObjectsReturned) as e:
            print("Error updating second event partner:", e)

def update_save_participant(request):
    if request.method == 'POST':
        print("i am in")
        user = request.session.get('username')
        loggedUser = get_object_or_404(Participant, whatsapp_number=user)
        
        name = request.POST.get('name')
        date_of_birth = request.POST.get('date_of_birth')
        city = request.POST.get('city')
        email = request.POST.get('email')
        indian_tree_tshirt_size = request.POST.get('indian_tree_tshirt_size')
        indian_tree_shorts_size = request.POST.get('indian_tree_shorts_size')
        food_preference = request.POST.get('food_preference')
        stay_arrangement = request.POST.get('stay_arrangement')
        first_event_name = request.POST.get('first_event')
        second_event_name = request.POST.get('second_event')
        first_event_category = request.POST.get('first_event_category')
        second_event_category = request.POST.get('second_event_category')

        first_event_category = request.POST.get('first_event_category')
        second_event_category = request.POST.get('second_event_category')

        # Check if the participant's category matches the category of both event partners
        if (loggedUser.first_event_partner != 'Not Registered' and 
            loggedUser.first_event_category != first_event_category):
            messages.error(request, "Participant's category does not match the category of the first event partner.")
            return redirect('detail')
        
        if (loggedUser.second_event_partner != 'Not Registered' and 
            loggedUser.second_event_category != second_event_category):
            messages.error(request, "Participant's category does not match the category of the second event partner.")
            return redirect('detail')
        
        user_age = calculate_age(date_of_birth)
        print("First event name:", first_event_name)
        print("Second event name:", second_event_name)

        first_event_id = None
        second_event_id = None

        if first_event_name == "Not Registered" or first_event_name == 'Not Registered-Not Registered':
            first_event_name = "Not Registered"
            first_event_id = "Not Registered"
        if second_event_name == "Not Registered" or second_event_name == 'Not Registered-Not Registered':
            second_event_id = "Not Registered"
            second_event_name = "Not Registered"

        if first_event_name != 'Not Registered' and first_event_name != 'Not Registered-Not Registered':
            first_event_partner_detail = get_object_or_404(Participant, name=first_event_name, participant_id=loggedUser.first_event_id)
            first_event_partner_age = calculate_age(first_event_partner_detail.date_of_birth)
            if not check_age_requirements(user_age, first_event_partner_age, first_event_category):
                messages.error(request, "Your and First Event Partner's age do not meet the requirements.")
                return redirect('detail')

            first_event_id = first_event_partner_detail.participant_id

        if second_event_name != 'Not Registered' and second_event_name != 'Not Registered-Not Registered':
            try:
                second_event_partner_detail = Participant.objects.get(name=second_event_name, participant_id=loggedUser.second_event_id)
            except Participant.DoesNotExist:
                messages.error(request, "Participant with the specified details not found.")
                return redirect('detail')
            second_event_partner_age = calculate_age(second_event_partner_detail.date_of_birth)
            if not check_age_requirements(user_age, second_event_partner_age, second_event_category):
                messages.error(request, "Your and Second Event Partner's age do not meet the requirements.")
                return redirect('detail')

            second_event_id = second_event_partner_detail.participant_id

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

        try:
            loggedUser.save()

            uuupdate_event_partners(loggedUser)

            messages.success(request, 'Participant information updated successfully.')
            return redirect('detail')
        except Exception as e:
            print(e)
            messages.error(request, 'Failed to update participant information.')
            return redirect('detail')
    else:
        return HttpResponseNotAllowed(['POST'])