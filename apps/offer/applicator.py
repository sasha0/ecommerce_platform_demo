from oscar.apps.offer.applicator import Applicator as OriginalApplicator


class Applicator(OriginalApplicator):
    def get_user_offers(self, user):
        if user.membership:
            return [user.membership.offer]
