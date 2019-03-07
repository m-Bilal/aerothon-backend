from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tags(models.Model):
    tag_name = models.CharField(max_length=100)

    def __str__(self):
        return self.tag_name


class Headline(models.Model):
    headline = models.CharField(max_length=50, null=True)
    brief = models.CharField(max_length=100, null=True)
    story = models.TextField(null=True)
    image = models.TextField(null=True)
    #tags = models.ManyToManyField(Tags, null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)

    def __str__(self):
        return self.headline


class AircraftModel(models.Model):
    name = models.CharField(max_length=32, null=False, blank=False, default='null')
    gross_weight = models.IntegerField(null=False, blank=False, default=0)
    fuel_capacity_left_wing = models.IntegerField(null=False, blank=False, default=0)
    fuel_capacity_right_wing = models.IntegerField(null=False, blank=False, default=0)
    maximum_altitude = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.name


class Aircraft(models.Model):
    msn = models.CharField(max_length=32, unique=True, null=False, blank=False)
    harness_length = models.IntegerField(null=False, blank=False)
    model = models.ForeignKey(AircraftModel, on_delete=models.CASCADE, null=False, blank=False)
    make_year = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.model.name + ' ' + self.msn


class Airport(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False, unique=True)
    country = models.CharField(max_length=64, null=False, blank=False)
    city = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.name + ', ' + self.city + ', ' + self.country


class Flight(models.Model):
    flight_no = models.CharField(max_length=64, unique=True, null=False, blank=False)
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, null=False, blank=False)
    planned_destination_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, null=False, blank=False, related_name="plnd_dest_airport")
    actual_destination_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, null=False, blank=False, related_name="act_dest_airport")
    diversion_reason = models.CharField(max_length=100)
    atmospheric_pressure = models.IntegerField(null=False, blank=False)
    room_temp = models.IntegerField(null=False, blank=False)
    max_altitude_reached = models.IntegerField(null=False, blank=False)
    departure_time = models.TimeField(null=False, blank=False)
    planned_arrival_time = models.TimeField(null=False, blank=False)
    actual_arrival_time = models.TimeField(null=False, blank=False)
    departure_date = models.DateField(null=False, blank=False)
    planned_arrival_date = models.DateField(null=False, blank=False)
    actual_arrival_date = models.DateField(null=False, blank=False)
    abberation = models.BooleanField(null=False, blank=False)
    emergency = models.BooleanField(null=False, blank=False)
    abberation_reason = models.TextField()
    emergency_reason = models.TextField()
    luggage_weight = models.IntegerField(null=False, blank=False)
    passenger_strength = models.IntegerField(null=False, blank=False)
    cabin_crew_strength = models.IntegerField(null=False, blank=False)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.flight_no


