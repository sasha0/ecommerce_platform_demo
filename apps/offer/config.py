from oscar.apps.offer import config


class OfferConfig(config.OfferConfig):
    name = 'apps.offer'

    def ready(self):
        from . import receivers  # noqa
