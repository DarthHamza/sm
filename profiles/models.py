from django.db import models
from django.contrib.auth.models import User


class Follow(models.Model):
    # stalker will give me who I'm following
    stalker = models.ForeignKey(User, related_name="stalker", on_delete=models.CASCADE)
    # prey will give me who is following me
    prey = models.ForeignKey(User, related_name="prey", on_delete=models.CASCADE)
