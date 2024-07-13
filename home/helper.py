from home.models import Participant,TeamForFirstEvent, TeamForSecondEvent
# ,category
from datetime import datetime,date
from .models import category  # Import your Category model

def create_teams_for_events(participant, first_event_partner_detail=None, second_event_partner_detail=None, first_event_category=None, second_event_category=None):
    print("Creating teams for events...")
    print("Participant:", participant)
    print("First Event Partner Detail:", first_event_partner_detail)
    print("Second Event Partner Detail:", second_event_partner_detail)
    
    # Fetch or create the category instances for the events
    first_event_name = first_event_category
    print("first_event_name:", first_event_name)
    second_event_name = second_event_category
    print("second_event_name:", second_event_name)

    first_event_category_instance, created_first = category.objects.get_or_create(Event_category=first_event_name)
    second_event_category_instance, created_second = category.objects.get_or_create(Event_category=second_event_name)

    print("first_event_category_instance:", first_event_category_instance)
    print("second_event_category_instance:", second_event_category_instance)

    if first_event_partner_detail and second_event_partner_detail:
        team_for_first_event = TeamForFirstEvent.objects.create(
            first_partner=participant,
            second_partner=first_event_partner_detail,
            event=first_event_category_instance
        )
        print("Team for First Event Created:", team_for_first_event)
        
        team_for_second_event = TeamForSecondEvent.objects.create(
            first_partner=participant,
            second_partner=second_event_partner_detail,
            event=second_event_category_instance
        )
        print("Team for Second Event Created:", team_for_second_event)
    elif first_event_partner_detail!="Not Registered Yet":
        # Create team only for the first event
        team_for_first_event = TeamForFirstEvent.objects.create(
            first_partner=participant,
            second_partner=first_event_partner_detail,
            event=first_event_category_instance
        )
        print("Team for First Event Created:", team_for_first_event)
    elif second_event_partner_detail!="Not Registered Yet":
        # Create team only for the second event
        team_for_second_event = TeamForSecondEvent.objects.create(
            first_partner=participant,
            second_partner=second_event_partner_detail,
            event=second_event_category_instance
        )
        print("Team for Second Event Created:", team_for_second_event)



# Example usage:
# create_teams_for_events(participant=Rinki, first_event_partner_detail=Mansi, second_event_partner_detail=Ramit)

# Example usage:
# create_teams_for_events(participant=Rinki, first_event_partner_detail=Mansi, second_event_partner_detail=Ramit)

# Example usage:
# create_teams_for_events(participant=Rinki, first_event_partner_detail=Mansi, second_event_partner_detail=Ramit)





def update_team_events(participant):
    print("Updating teams for participant:", participant)

    # Fetch the event categories for the participant
    first_event_category_instance, created_first = category.objects.get_or_create(Event_category=participant.first_event_category)
    second_event_category_instance, created_second = category.objects.get_or_create(Event_category=participant.second_event_category)

    # Update or create the team for the first event
    if participant.first_event_partner != 'Not Registered Yet':
        try:
            first_event_partner_detail = Participant.objects.get(name=participant.first_event_partner, participant_id=participant.first_event_id)
            TeamForFirstEvent.objects.update_or_create(
                first_partner=participant,
                defaults={
                    'second_partner': first_event_partner_detail,
                    'event': first_event_category_instance
                }
            )
            print("Updated team for first event.")
        except Participant.DoesNotExist:
            print("First event partner does not exist.")
    else:
        # Delete the team if the participant is not registered
        TeamForFirstEvent.objects.filter(first_partner=participant).delete()
        TeamForFirstEvent.objects.filter(second_partner=participant).delete()
        print("Deleted team for first event where participant is first or second partner.")

    # Update or create the team for the second event
    if participant.second_event_partner != 'Not Registered Yet':
        try:
            second_event_partner_detail = Participant.objects.get(name=participant.second_event_partner, participant_id=participant.second_event_id)
            TeamForSecondEvent.objects.update_or_create(
                first_partner=participant,
                defaults={
                    'second_partner': second_event_partner_detail,
                    'event': second_event_category_instance
                }
            )
            print("Updated team for second event.")
        except Participant.DoesNotExist:
            print("Second event partner does not exist.")
    else:
        # Delete the team if the participant is not registered
        TeamForSecondEvent.objects.filter(first_partner=participant).delete()
        TeamForSecondEvent.objects.filter(second_partner=participant).delete()
        print("Deleted team for second event where participant is first or second partner.")

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

def uuupdate_event_partners_to_not_registered_ist(first_event_partner_for_update, first_event_id_for_update):
    try:
        first_event_partner = Participant.objects.get(name=first_event_partner_for_update, participant_id=first_event_id_for_update)
        first_event_partner.first_event_id = "Not Registered Yet"
        first_event_partner.first_event_partner = "Not Registered Yet"
        first_event_partner.save()
    except Participant.DoesNotExist:
        print(f"Participant with name '{first_event_partner_for_update}' and ID '{first_event_id_for_update}' does not exist.")
    except Participant.MultipleObjectsReturned:
        print(f"Multiple participants found with name '{first_event_partner_for_update}' and ID '{first_event_id_for_update}'. Update failed.")
    except Exception as e:
        print(f"Error updating first event partner: {e}")

def uuupdate_event_partners_to_not_registered_scnd(second_event_partner_for_update, second_event_id_for_update):
    try:
        second_event_partner = Participant.objects.get(name=second_event_partner_for_update, participant_id=second_event_id_for_update)
        second_event_partner.second_event_id = "Not Registered Yet"
        second_event_partner.second_event_partner = "Not Registered Yet"
        second_event_partner.save()
    except Participant.DoesNotExist:
        print(f"Participant with name '{second_event_partner_for_update}' and ID '{second_event_id_for_update}' does not exist.")
    except Participant.MultipleObjectsReturned:
        print(f"Multiple participants found with name '{second_event_partner_for_update}' and ID '{second_event_id_for_update}'. Update failed.")
    except Exception as e:
        print(f"Error updating second event partner: {e}")

def uuupdate_event_partners_ist(participant):
    first_event_name = participant.first_event_partner
    first_event_id = participant.first_event_id

    if first_event_name not in ["Not Registered Yet", "Not Registered Yet-Not Registered Yet"] and first_event_id not in ["Not Registered Yet", "Not Registered Yet-Not Registered Yet"]:
        try:
            first_event_partner = Participant.objects.get(name=first_event_name, participant_id=first_event_id)
            first_event_partner.first_event_id = participant.participant_id
            first_event_partner.first_event_partner = participant.name
            first_event_partner.save()
        except Participant.DoesNotExist:
            print(f"Participant with name '{first_event_name}' and ID '{first_event_id}' does not exist.")
        except Participant.MultipleObjectsReturned:
            print(f"Multiple participants found with name '{first_event_name}' and ID '{first_event_id}'. Update failed.")
        except Exception as e:
            print(f"Error updating first event partner: {e}")

def uuupdate_event_partners_scnd(participant):
    second_event_name = participant.second_event_partner
    second_event_id = participant.second_event_id

    if second_event_name not in ["Not Registered Yet", "Not Registered Yet-Not Registered Yet"] and second_event_id not in ["Not Registered Yet", "Not Registered Yet-Not Registered Yet"]:
        try:
            second_event_partner = Participant.objects.get(name=second_event_name, participant_id=second_event_id)
            second_event_partner.second_event_id = participant.participant_id
            second_event_partner.second_event_partner = participant.name
            second_event_partner.save()
        except Participant.DoesNotExist:
            print(f"Participant with name '{second_event_name}' and ID '{second_event_id}' does not exist.")
        except Participant.MultipleObjectsReturned:
            print(f"Multiple participants found with name '{second_event_name}' and ID '{second_event_id}'. Update failed.")
        except Exception as e:
            print(f"Error updating second event partner: {e}")
