from django.contrib import admin

from .models import Membership

admin.site.register(Membership)


from oscar.apps.offer.admin import *  # noqa
