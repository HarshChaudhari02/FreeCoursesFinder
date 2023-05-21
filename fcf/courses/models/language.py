from django.db import models

class Language(models.Model):

    name = models.CharField(max_length=500)

    @staticmethod
    def get_all_language():
        return Language.objects.all()

    def __str__(self):
        return self.name