from django.core.management.base import BaseCommand
from home.models import Participant, EventCategory

class Command(BaseCommand):
    help = 'Populate EventCategory model for existing participants'

    def handle(self, *args, **kwargs):
        participants = Participant.objects.all()
        self.stdout.write(f"Found {participants.count()} participants.")

        for participant in participants:
            self.stdout.write(f"Processing participant: {participant.name} (ID: {participant.participant_id})")

            # Process first event
            if participant.first_event_partner and participant.first_event_partner != "Not Registered Yet":
                self.stdout.write(f"  Adding first event for {participant.name}")
                EventCategory.objects.update_or_create(
                    participant=participant,
                    event_type='first',
                    defaults={
                        'category': participant.first_event_category,
                        'partner': participant.first_event_partner,
                        'event_id': participant.first_event_id,
                    }
                )

            # Process second event
            if participant.second_event_partner and participant.second_event_partner != "Not Registered Yet":
                self.stdout.write(f"  Adding second event for {participant.name}")
                EventCategory.objects.update_or_create(
                    participant=participant,
                    event_type='second',
                    defaults={
                        'category': participant.second_event_category,
                        'partner': participant.second_event_partner,
                        'event_id': participant.second_event_id,
                    }
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated EventCategory model for existing participants.'))
