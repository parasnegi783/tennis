import random
from datetime import datetime, timedelta

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

def generate_test_data():
    categories = ['Open', '90+', '105+', '120+']
    participants = []
    current_date = datetime.now()

    for category in categories:
        for _ in range(20):
            if category == 'Open':
                age = random.randint(31, 50)
                partner_age = random.randint(31, 50)
                category_name = 'Open'
            elif category == '90+':
                age = random.randint(31, 50)
                partner_age = random.randint(31, 50)
                while age + partner_age < 90:
                    partner_age = random.randint(31, 50)
                category_name = '90+'
            elif category == '105+':
                age = random.randint(31, 50)
                partner_age = random.randint(31, 50)
                while age + partner_age < 105:
                    partner_age = random.randint(31, 50)
                category_name = '105+'
            elif category == '120+':
                age = random.randint(31, 50)
                partner_age = random.randint(31, 50)
                while age + partner_age < 120:
                    partner_age = random.randint(31, 50)
                category_name = '120+'

            dob = current_date - timedelta(days=age * 365)
            partner_dob = current_date - timedelta(days=partner_age * 365)

            participant = {
                'name': f'Participant_{category}_{_}',
                'date_of_birth': dob.date(),
                'whatsapp_number': f'+9100000000{random.randint(10, 99)}',
                'city': 'City_' + category,
                'email': f'participant_{category}_{_}@example.com',
                'indian_tree_tshirt_size': random.choice(['S', 'M', 'L', 'XL']),
                'indian_tree_shorts_size': random.choice(['S', 'M', 'L', 'XL']),
                'food_preference': random.choice(['Veg', 'Non-Veg']),
                'stay_arrangement': random.choice(['Yes', 'No']),
                'first_event_partner': f'Partner_{category}_{_}',
                'first_event_category': category_name,
                'first_event_id': str(random.randint(1000, 9999)),
                'second_event_partner': f'SecondPartner_{category}_{_}',
                'second_event_category': category_name,
                'second_event_id': str(random.randint(1000, 9999)),
            }
            
            partner = {
                'name': f'Partner_{category}_{_}',
                'date_of_birth': partner_dob.date(),
                'whatsapp_number': f'+9100000000{random.randint(10, 99)}',
                'city': 'City_' + category,
                'email': f'partner_{category}_{_}@example.com',
                'indian_tree_tshirt_size': random.choice(['S', 'M', 'L', 'XL']),
                'indian_tree_shorts_size': random.choice(['S', 'M', 'L', 'XL']),
                'food_preference': random.choice(['Veg', 'Non-Veg']),
                'stay_arrangement': random.choice(['Yes', 'No']),
                'first_event_partner': f'Participant_{category}_{_}',
                'first_event_category': category_name,
                'first_event_id': str(random.randint(1000, 9999)),
                'second_event_partner': f'SecondPartner_{category}_{_}',
                'second_event_category': category_name,
                'second_event_id': str(random.randint(1000, 9999)),
            }

            participants.append(participant)
            participants.append(partner)
    
    return participants

# Generating test data
test_data = generate_test_data()

# Print the test data
for data in test_data:
    print(data)
