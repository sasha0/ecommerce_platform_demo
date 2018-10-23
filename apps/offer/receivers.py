from django.db.models import Sum
from django.dispatch import receiver

from oscar.apps.order.signals import order_placed


@receiver(order_placed)
def receive_order_placed(sender, order, user, **kwargs):
    if order.lines.filter(product__bonus_points__gt=0).count() > 0:
        user.bonus_points += order.lines.filter(product__bonus_points__gt=0)\
            .aggregate(total_bonus_points=Sum('product__bonus_points'))['total_bonus_points']
        user.save()
