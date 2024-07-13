from django.test import TestCase
from home.models import Participant, TeamForFirstEvent, TeamForSecondEvent, Category

class ParticipantModelTests(TestCase):

    def setUp(self):
        self.category1 = Category.objects.create(event_category="Open")
        self.category2 = Category.objects.create(event_category="90+")

    def test_create_participant_and_teams(self):
        participant = Participant.objects.create(
            name="Test Participant",
            date_of_birth="1990-01-01",
            whatsapp_number="1234567890",
            city="Test City",
            email="test@example.com",
            indian_tree_tshirt_size="M",
            indian_tree_shorts_size="L",
            food_preference="Vegetarian",
            stay_arrangement="Yes",
            first_event_partner="Partner A",
            first_event_category="Open",
            first_event_id="1",
            second_event_partner="Partner B",
            second_event_category="90+",
            second_event_id="2"
        )

        first_event_partner = Participant.objects.create(
            name="Partner A",
            date_of_birth="1985-01-01",
            whatsapp_number="0987654321",
            city="Test City",
            email="partnerA@example.com",
            indian_tree_tshirt_size="M",
            indian_tree_shorts_size="L",
            food_preference="Vegetarian",
            stay_arrangement="Yes"
        )

        second_event_partner = Participant.objects.create(
            name="Partner B",
            date_of_birth="1980-01-01",
            whatsapp_number="1122334455",
            city="Test City",
            email="partnerB@example.com",
            indian_tree_tshirt_size="M",
            indian_tree_shorts_size="L",
            food_preference="Vegetarian",
            stay_arrangement="Yes"
        )

        team_for_first_event = TeamForFirstEvent.objects.create(
            first_partner=participant,
            second_partner=first_event_partner,
            event=self.category1
        )

        team_for_second_event = TeamForSecondEvent.objects.create(
            first_partner=participant,
            second_partner=second_event_partner,
            event=self.category2
        )

        self.assertEqual(TeamForFirstEvent.objects.count(), 1)
        self.assertEqual(TeamForSecondEvent.objects.count(), 1)
        self.assertEqual(team_for_first_event.event.event_category, "Open")
        self.assertEqual(team_for_second_event.event.event_category, "90+")
