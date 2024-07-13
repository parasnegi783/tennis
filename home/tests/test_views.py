from django.test import TestCase, Client
from django.urls import reverse
from home.models import Participant, TeamForFirstEvent, TeamForSecondEvent, category,User

class ParticipantViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.user_data = {
            'name': 'Test Participant',
            'date_of_birth': '1990-01-01',
            'whatsapp_number': '1234567890',
            'city': 'Test City',
            'email': 'test@example.com',
            'indian_tree_tshirt_size': 'M',
            'indian_tree_shorts_size': 'L',
            'food_preference': 'Vegetarian',
            'stay_arrangement': 'Yes',
            'first_event': 'Partner A-1',
            'second_event': 'Partner B-2',
            'first_event_category': 'Open',
            'second_event_category': '90+'
        }

    def test_save_participant(self):
        response = self.client.post(self.register_url, data=self.user_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Participant.objects.filter(whatsapp_number='1234567890').exists())
        self.assertTrue(User.objects.filter(username='1234567890').exists())
