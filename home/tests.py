from django.test import TestCase
from .models import Participant, TeamForFirstEvent, TeamForSecondEvent
from .views import create_teams_for_events

class CreateTeamsForEventsTests(TestCase):

    def setUp(self):
        # Set up any necessary data for testing
        self.participant = Participant.objects.create(name='Participant 1', date_of_birth='1990-01-01')
        self.partner1 = Participant.objects.create(name='Partner 1', date_of_birth='1995-01-01')
        self.partner2 = Participant.objects.create(name='Partner 2', date_of_birth='1992-01-01')

    def test_create_teams_for_both_events(self):
        create_teams_for_events(self.participant, self.partner1, self.partner2)
        
        # Check if teams were created for both events
        teams_first_event = TeamForFirstEvent.objects.filter(first_partner=self.participant).count()
        teams_second_event = TeamForSecondEvent.objects.filter(first_partner=self.participant).count()
        
        self.assertEqual(teams_first_event, 1)
        self.assertEqual(teams_second_event, 1)

    def test_create_team_for_first_event_only(self):
        create_teams_for_events(self.participant, self.partner1)
        
        # Check if team was created only for the first event
        teams_first_event = TeamForFirstEvent.objects.filter(first_partner=self.participant).count()
        teams_second_event = TeamForSecondEvent.objects.filter(first_partner=self.participant).count()
        
        self.assertEqual(teams_first_event, 1)
        self.assertEqual(teams_second_event, 0)

    def test_create_team_for_second_event_only(self):
        create_teams_for_events(self.participant, second_event_partner_detail=self.partner2)
        
        # Check if team was created only for the second event
        teams_first_event = TeamForFirstEvent.objects.filter(first_partner=self.participant).count()
        teams_second_event = TeamForSecondEvent.objects.filter(first_partner=self.participant).count()
        
        self.assertEqual(teams_first_event, 0)
        self.assertEqual(teams_second_event, 1)
