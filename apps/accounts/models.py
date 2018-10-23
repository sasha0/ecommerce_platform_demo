from decimal import Decimal as D

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    membership = models.ForeignKey('offer.Membership', on_delete=models.CASCADE, null=True, blank=True)
    bonus_points = models.DecimalField(max_digits=12, decimal_places=2, default=D(0))
