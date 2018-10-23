from django.db import models

from django.utils.timezone import now


class SalePrice(models.Model):
    stockrecord = models.OneToOneField(
        'partner.StockRecord', on_delete=models.CASCADE)
    price_excl_tax = models.DecimalField(decimal_places=2, max_digits=12)
    valid_from = models.DateTimeField()
    valid_til = models.DateTimeField()

    def is_valid(self):
        return self.valid_from <= now() and self.valid_til > now()

    def __str__(self):
        return '%s - %s' % (self.stockrecord, self.price_excl_tax)

from oscar.apps.partner.models import *  # noqa isort:skip
