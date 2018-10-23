from django.db import models


from oscar.apps.offer.abstract_models import AbstractConditionalOffer, AbstractCondition


class EmptyCondition(AbstractCondition):
    def is_satisfied(self, offer, basket):
        return True

    def is_partially_satisfied(self, offer, basket):
        return True

    def proxy(self):
        return self


class ConditionalOffer(AbstractConditionalOffer):
    condition = models.ForeignKey(
        'offer.Condition', on_delete=models.CASCADE, related_name='offers', null=True, blank=True)

    def is_condition_satisfied(self, basket):
        if not self.condition:
            return True
        return super().is_condition_satisfied(basket)

    def is_condition_partially_satisfied(self, basket):
        if not self.condition:
            return True
        return super().is_condition_partially_satisfied(basket)

    def apply_benefit(self, basket):
        if self.condition and not self.is_condition_satisfied(basket):
            return ZERO_DISCOUNT

        if not self.condition:
            return self.benefit.proxy().apply(basket, EmptyCondition(), self)
        return self.benefit.proxy().apply(
            basket, self.condition.proxy(), self)

    def get_upsell_message(self, basket):
        if not self.condition:
            return None
        return super().get_upsell_message(basket)


class Membership(models.Model):
    title = models.CharField(max_length=255)
    offer = models.ForeignKey('offer.ConditionalOffer', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


from oscar.apps.offer.models import *  # noqa isort:skip
