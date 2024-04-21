from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    # HOST = 'Host'
    # RSVP = 'Rsvp'
    # USER_TYPES = [
    #     (HOST, 'Host'),
    #     (RSVP, 'Rsvp'),
    # ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile_image_url = models.URLField(blank=True, null=True)
    # type = models.CharField(max_length=4, choices=USER_TYPES, default=RSVP)
