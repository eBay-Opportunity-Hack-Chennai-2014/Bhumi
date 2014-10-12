from django.contrib import admin
from nakshatra.models import Event, MajorCategory, Category, \
    Organization, Participant, EventEnrollment, \
    City, Location

# Register your models here.


class ParticipantAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'name',
        'age',
        'gender',
    )

    def image_img(self):
        return u'<img src="%s" />' % self.image
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'eventName',
        'city',
    )


class CityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
    )


class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
    )


class EventEnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        'event',
        'participants'
    )

admin.site.register(Event, EventAdmin)
admin.site.register(MajorCategory)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(EventEnrollment, EventEnrollmentAdmin)
admin.site.register(City, CityAdmin)
