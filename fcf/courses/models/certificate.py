from django.db import models

class Certificate(models.Model):
    name = models.CharField(max_length=500)

    @staticmethod
    def get_all_certificate():
        return Certificate.objects.all()

    def __str__(self):
        return self.name