from decimal import Decimal as D

from django.db import models

from oscar.apps.catalogue.abstract_models import AbstractProduct


class Product(AbstractProduct):
    bonus_points = models.DecimalField(max_digits=12, decimal_places=2, default=D(0))


from oscar.apps.catalogue.models import *  # noqa isort:skip
