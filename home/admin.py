from django.contrib import admin
from .models import Participant,card,Event,BankDetail,PaymentInfo,TeamForFirstEvent,TeamForSecondEvent,category

# admin.site.register(Participant)
admin.site.register(card)
admin.site.register(Event)
admin.site.register(BankDetail)
admin.site.register(PaymentInfo)
admin.site.register(category)
class FirstEventPartnerFilter(admin.SimpleListFilter):
    title = 'First Event Partner'
    parameter_name = 'first_event_partner'

    def lookups(self, request, model_admin):
        return (
            ('Not Registered Yet', 'Not Registered Yet'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'Not Registered Yet':
            return queryset.filter(first_event_partner__isnull=True)

class SecondEventPartnerFilter(admin.SimpleListFilter):
    title = 'Second Event Partner'
    parameter_name = 'second_event_partner'

    def lookups(self, request, model_admin):
        return (
            ('Not Registered Yet', 'Not Registered Yet'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'Not Registered Yet':
            return queryset.filter(second_event_partner__isnull=True)

class ParticipantAdmin(admin.ModelAdmin):
    list_filter = (
        'indian_tree_tshirt_size',
        'indian_tree_shorts_size',
        'city',
        'food_preference',
        'stay_arrangement',
        'first_event_category',
        'second_event_category',
        FirstEventPartnerFilter,
        SecondEventPartnerFilter,
    )

admin.site.register(Participant, ParticipantAdmin)

class TeamForFirstEventAdmin(admin.ModelAdmin):
    list_filter = ('first_partner', 'second_partner', 'event')
admin.site.register(TeamForFirstEvent, TeamForFirstEventAdmin)

class TeamForSecondEventAdmin(admin.ModelAdmin):
    list_filter = ('first_partner', 'second_partner', 'event')
admin.site.register(TeamForSecondEvent, TeamForSecondEventAdmin)



