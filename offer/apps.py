from django.apps import AppConfig


class OfferConfig(AppConfig):
    name = "offer"

    def ready(self):
        from . import signals
