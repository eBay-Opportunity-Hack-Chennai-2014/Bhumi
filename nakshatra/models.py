from django.db import models
from bsddb.test.test_all import verbose

# Create your models here.

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)

EVENT_TYPE = (
    ('I', 'Indivigual'),
    ('G', 'Group'),
)

CATEGORY_LEVEL = (
    ('S', 'Senior'),
    ('SS', 'Super Senior'),
    ('J', 'Junior'),
)
class MajorCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name="Major Category Name")
    
    class Meta:
        verbose_name = "MajorCategory"
        verbose_name_plural = "MajorCategories"


class MinorCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name="Minor Category Name")
    
    class Meta:
        verbose_name = "MinorCategory"
        verbose_name_plural = "MinorCategories"


class Location(models.Model):
    name = models.CharField(max_length=150, verbose_name="Location Name")


class City(models.Model):
    name = models.CharField(max_length=75, verbose_name="City Name")
    location = models.ForeignKey(
        Location,
        verbose_name="Location Name"
    )
    
    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

class Organization(models.Model):
    name = models.CharField(max_length=75, verbose_name="Organization Name")
    location = models.ForeignKey(
        Location,
        verbose_name="Location Name"
    )
    
class Participant(models.Model):
    name = models.CharField(max_length=75, verbose_name="Participant Name")
    dob = models.DateField(verbose_name="Date Of Birth")
    age = models.IntegerField(verbose_name="Age")
    gender = models.CharField(
        max_length=2,
        choices=GENDER,
        default='M',
        verbose_name='Gender'
    )
    interest = models.TextField(max_length=150, verbose_name="Participant Interest")
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_LEVEL,
        default='J',
        verbose_name='Category Level'
    )
        

class Event(models.Model):
    eventName = models.CharField(max_length=50, verbose_name="Event Name")
    desc = models.TextField(max_length=150, verbose_name="Description")
    majorCategory = models.ForeignKey(
        MajorCategory,
        verbose_name="Major Category"
    )
    minorCategory = models.ForeignKey(
        MinorCategory,
        verbose_name="Minor Category"
    )
    eventType = models.CharField(
        max_length=2,
        choices=EVENT_TYPE,
        default='I',
        verbose_name='Event Type'
    )
    gender = models.CharField(
        max_length=2,
        choices=GENDER,
        default='M',
        verbose_name='Gender'
    )
    city = models.ForeignKey(
        City,
        default=None,
        verbose_name="City Name"
    )
    minP = models.IntegerField(default=None, verbose_name="Minimum Participant")
    maxP = models.IntegerField(default=None, verbose_name="Maximum Participant")
    
class EventEnrollment(models.Model):
    event = models.ForeignKey(
        Event,
        verbose_name="Event"
    )
    participants = models.ForeignKey(
        Participant,
        verbose_name="Minor Category"
    )

