from django.apps import AppConfig


class FakeRestAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fake_rest_app'
