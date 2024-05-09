from django.shortcuts import render,redirect
from .models import Participant,FirstEvent,SecondEvent,card
import random
import oracledb
import datetime

# to connect oracle database
conn = oracledb.connect(user='tennisdba', password='password', host="localhost", port=1521)

list1=[]
#function to generate random id for first_event
def generate1(value):
    random_number = random.randint(1, 9999)
    if random_number not in value:
        return random_number
    else:
        generate1(value)

list2=[]
#function to generate random id for second_event
def generate2(value):
    random_number = random.randint(1, 9999)
    if random_number not in value:
        return random_number
    else:
        generate2(value)

list2=[]
#function to generate random id for participants
def generate_id(participant_ids):
    random_number = random.randint(1, 9999)
    if random_number not in participant_ids:
        return random_number
    else:
        generate_id()
    

def home(request):
    cards = card.objects.all()
    return render(request, 'home.html', {'cards': cards})

def register(request):
    return render(request,'form1.html')


def save_participant(request):
    if request.method == 'POST':
        participant_ids = list(Participant.objects.values_list('participant_id', flat=True))
        print("values",participant_ids)
        participant_id=generate_id(participant_ids)
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
        second_event_name = request.POST.get('second_event')



        request.session['participant_id'] = participant_id
        request.session['name'] = name
        request.session['date_of_birth'] = date_of_birth
        request.session['whatsapp_number'] = whatsapp_number
        request.session['city'] = city
        request.session['email'] = email
        request.session['indian_tree_tshirt_size'] = indian_tree_tshirt_size
        request.session['indian_tree_shorts_size'] = indian_tree_shorts_size
        request.session['food_preference'] = food_preference
        request.session['stay_arrangement'] = stay_arrangement
        request.session['first_event'] = first_event_name
        request.session['second_event'] = second_event_name

        return render(request,'form2.html')
    # elif request.method == 'GET':
    #     return render(request,home.html)
    else:
        return render(request, 'form1.html')
    
def save_event1(request):
    if request.method == 'POST':
        first_event_choice = request.POST.get('first_event')
        first_event_partner = request.POST.get('first_partner')
        p1_indian_tree_tshirt_size = request.POST.get('p1_indian_tree_tshirt_size')
        p1_indian_tree_shorts_size = request.POST.get('p1_indian_tree_shorts_size')
        p1_food_preference = request.POST.get('p1_food_preference')
        p1_stay_arrangement = request.POST.get('p1_stay_arrangement')

        request.session['first_event_choice'] = first_event_choice
        request.session['first_event_partner'] = first_event_partner
        request.session['p1_indian_tree_tshirt_size'] = p1_indian_tree_tshirt_size
        request.session['p1_indian_tree_shorts_size'] = p1_indian_tree_shorts_size
        request.session['p1_food_preference'] = p1_food_preference
        request.session['p1_stay_arrangement'] = p1_stay_arrangement

        return render(request, 'form3.html')
    elif request.method == 'GET':
        return render(request, 'form2.html')
    else:
        return render(request, 'form2.html')
    

def save_event2(request):
    if request.method == 'POST':
        second_event_choice = request.POST.get('second_event')
        second_event_partner = request.POST.get('second_partner')
        p2_indian_tree_tshirts_size = request.POST.get('p2_indian_tree_tshirts_size')
        p2_indian_tree_shorts_size = request.POST.get('p2_indian_tree_shorts_size')
        p2_food_preference = request.POST.get('p2_food_preference')
        p2_stay_arrangement = request.POST.get('p2_stay_arrangement')

        request.session['second_event_choice'] = second_event_choice
        request.session['second_event_partner'] = second_event_partner
        request.session['p2_indian_tree_tshirts_size'] = p2_indian_tree_tshirts_size
        request.session['p2_indian_tree_shorts_size'] = p2_indian_tree_shorts_size
        request.session['p2_food_preference'] = p2_food_preference
        request.session['p2_stay_arrangement'] = p2_stay_arrangement
        if request.method == 'GET':
            return render(request, 'form2.html')
        else:    
            return final_save(request)
    
    else:
        return render(request, 'form3.html')


def final_save(request):
    if request.method=='POST':

        participant_id = request.session.get('participant_id')
        name = request.session.get('name')
        date_of_birth = request.session.get('date_of_birth')
        whatsapp_number = request.session.get('whatsapp_number')
        city = request.session.get('city')
        email = request.session.get('email')
        indian_tree_tshirt_size = request.session.get('indian_tree_tshirt_size')
        indian_tree_shorts_size = request.session.get('indian_tree_shorts_size')
        food_preference = request.session.get('food_preference')
        stay_arrangement = request.session.get('stay_arrangement')
        
        first_event_choice = request.session.get('first_event_choice')
        first_event_partner = request.session.get('first_event_partner')
        p1_indian_tree_tshirt_size = request.session.get('p1_indian_tree_tshirt_size')
        p1_indian_tree_shorts_size = request.session.get('p1_indian_tree_shorts_size')
        p1_food_preference = request.session.get('p1_food_preference')
        p1_stay_arrangement = request.session.get('p1_stay_arrangement')
        
        second_event_choice = request.session.get('second_event_choice')
        second_event_partner = request.session.get('second_event_partner')
        p2_indian_tree_tshirts_size = request.session.get('p2_indian_tree_tshirts_size')
        p2_indian_tree_shorts_size = request.session.get('p2_indian_tree_shorts_size')
        p2_food_preference = request.session.get('p2_food_preference')
        p2_stay_arrangement = request.session.get('p2_stay_arrangement')
        
        
        first_event_name = request.session.get('first_event')
        second_event_name = request.session.get('second_event')
        print(second_event_name)
        def Eventvalue1(value):
            x=0
            if value == "75+":
                x=1
            elif value == "90+":
                x=2
            elif value == "105+":
                x=3
            else:
                x=4
            return x
        first=Eventvalue1(first_event_name)
        print(first)
        def Eventvalue2(value):
            y=0
            if value == "75+":
                y=1
            elif value == "90+":
                y=2
            elif value == "105+":
                y=3
            else:
                y=4
            return y
        second=Eventvalue2(second_event_name)
        print(second)

        first_event = FirstEvent.objects.create(
            first_event_choice=first_event_choice,
            first_event_partner=first_event_partner,
            p1_indian_tree_tshirt_size=p1_indian_tree_tshirt_size,
            p1_indian_tree_shorts_size=p1_indian_tree_shorts_size,
            p1_food_preference=p1_food_preference,
            p1_stay_arrangement=p1_stay_arrangement
        )

        second_event = SecondEvent.objects.create(
            second_event_choice=second_event_choice,
            second_event_partner=second_event_partner,
            p2_indian_tree_tshirts_size=p2_indian_tree_tshirts_size,
            p2_indian_tree_shorts_size=p2_indian_tree_shorts_size,
            p2_food_preference=p2_food_preference,
            p2_stay_arrangement=p2_stay_arrangement
        )
        

        participant = Participant.objects.create(
            participant_id=participant_id,
            name=name,
            whatsapp_number=whatsapp_number,
            date_of_birth=date_of_birth,
            city=city,
            email=email,
            indian_tree_tshirt_size=indian_tree_tshirt_size,
            indian_tree_shorts_size=indian_tree_shorts_size,
            food_preference=food_preference,
            stay_arrangement=stay_arrangement,
            first_event=first_event,
            second_event=second_event
        )

        # inserting values in participant table

        if isinstance(date_of_birth, str):
            date_of_birth = datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')
        try:
            cur = conn.cursor()
            insert_query = """INSERT INTO PARTICIPANTS(id,name, whatsapp_number, date_of_birth, city, email, tshirt_size, shorts_size, food_preference, stay_arrangement, first_event_id, second_event_id) 
                              VALUES(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11,:12)"""
            result=cur.execute(insert_query, (participant_id,name, whatsapp_number, date_of_birth, city, email, indian_tree_tshirt_size, indian_tree_shorts_size, food_preference, stay_arrangement, first, second))
            conn.commit()
            print(result)
            print("Data inserted successfully")
        except oracledb.Error as error:
            print('Error occurred:', error)
        finally:
            if 'cur' in locals():
                cur.close()
            if 'conn' in locals():
                conn.close()

        # inserting value in first_event table
        try:
            connection = oracledb.connect(user='tennisdba', password='password', host="localhost", port=1521)


            cur2=conn.cursor()
            first_event_ids_list=list(cur2.execute("select first_event_id from firstevent"))
            first_event_id=generate1(first_event_ids_list)
            print(type(first_event_id))
            sql = """INSERT INTO FirstEvent 
                    (FIRST_EVENT_ID,EVENT_CHOICE, EVENT_PARTNER, TSHIRT_SIZE, SHORTS_SIZE, FOOD_PREFERENCE, STAY_ARRANGEMENT) 
                    VALUES(:FIRST_EVENT_ID,:EVENT_CHOICE, :EVENT_PARTNER, :TSHIRT_SIZE, :SHORTS_SIZE, :FOOD_PREFERENCE, :STAY_ARRANGEMENT)"""


            cursor = connection.cursor()


            cursor.execute(sql, {'FIRST_EVENT_ID':first_event_id,'EVENT_CHOICE':first_event_choice , 'EVENT_PARTNER': first_event_partner, 
                                'TSHIRT_SIZE': p1_indian_tree_tshirt_size, 
                                'SHORTS_SIZE': p1_indian_tree_shorts_size, 'FOOD_PREFERENCE': p1_food_preference, 
                                'STAY_ARRANGEMENT': p1_stay_arrangement})


            connection.commit()

            print("Data inserted into FirstEvent table successfully")

        except oracledb.Error as error:
            print('Error occurred:', error)






        try:

            cur2=conn.cursor()
            second_event_ids_list=list(cur2.execute("select second_event_id from secondevent"))
            second_event_id=generate1(second_event_ids_list)

            cursor = conn.cursor()

            sql = """INSERT INTO SecondEvent 
                    (Second_EVENT_ID,EVENT_CHOICE, EVENT_PARTNER, TSHIRT_SIZE, SHORTS_SIZE, FOOD_PREFERENCE, STAY_ARRANGEMENT) 
                    VALUES(:Second_EVENT_ID,:EVENT_CHOICE, :EVENT_PARTNER, :TSHIRT_SIZE, :SHORTS_SIZE, :FOOD_PREFERENCE, :STAY_ARRANGEMENT)"""

            cursor.execute(sql, {'Second_EVENT_ID':second_event_id,'EVENT_CHOICE':second_event_choice , 'EVENT_PARTNER': second_event_partner, 
                                'TSHIRT_SIZE': p2_indian_tree_tshirts_size, 
                                'SHORTS_SIZE': p2_indian_tree_shorts_size, 'FOOD_PREFERENCE': p2_food_preference, 
                                'STAY_ARRANGEMENT': p2_stay_arrangement})


            connection.commit()

            print("Data inserted into SecondEvent table successfully")

        except oracledb.Error as error:
            print('Error occurred:', error)


        request.session.clear()

        return render(request, 'home.html')
    else:
        return redirect('form1.html')



# conn = oracledb.connect(user='tennisdba', password='password', host="localhost", port=1521)
# cur = conn.cursor()
# insert_query = """INSERT INTO PARTICIPANTS
#                 (name, whatsapp_number, city, email, tshirt_size, shorts_size, food_preference, stay_arrangement, first_event_id, second_event_id) 
#                 VALUES('nav', '9898989898','asr', 'n@gmail.com', 'small',  'small', 'veg', 'no', 3, 4)"""
# # result=cur.execute(insert_query, (name, whatsapp_number, date_of_birth_str, city, email, indian_tree_tshirt_size, indian_tree_shorts_size, food_preference, stay_arrangement, first, second))
# result = cur.execute(insert_query)
# conn.commit()
# print(result)
# print("Data inserted successfully")




