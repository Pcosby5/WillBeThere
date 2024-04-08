from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Event(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    # items = models.JSONField()  # Array of strings
    items = models.TextField(max_length=200)
    eventImageUrl = models.URLField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"pk": self.pk})

class RSVP(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    congratulatoryMessage = models.TextField(blank=True, null=True)
    items = models.TextField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    attending = models.BooleanField()
    # additionalPeople = models.JSONField()  # Array of strings
    additionalPeople = models.TextField(max_length=200)

    def __str__(self):
        return self.name



# class Event(models.Model):
#     organizer = models.ForeignKey(User, on_delete=models.CASCADE)
#     email = models.EmailField()
#     title = models.CharField(max_length=100)
#     location = models.CharField(max_length=100, blank=True)
#     image = models.ImageField(upload_to='event_images/', null=True, blank=True)
#     date = models.DateField()
#     attendees = models.ManyToManyField(User, through='RSVP')

# class RSVP(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     email = models.EmailField()
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     plus_ones = models.PositiveIntegerField(default=0)
#     confirmed = models.BooleanField(default=False)



