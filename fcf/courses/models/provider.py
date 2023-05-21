from django.db import models

class Provider(models.Model):

    name = models.CharField(max_length=500)
    img = models.CharField(max_length=5000, default='', blank=True)
    description = models.CharField(max_length=10000, default='', blank=True)

    @staticmethod
    def get_all_provider():
        return Provider.objects.all()

    @staticmethod
    def get_all_provider_by_id(provider_id):
        return Provider.objects.filter(id=provider_id)

    def __str__(self):
        return self.name