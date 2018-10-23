from .models import SalePrice

from django.contrib import admin


admin.site.register(SalePrice)

from oscar.apps.partner.admin import *  # noqa
