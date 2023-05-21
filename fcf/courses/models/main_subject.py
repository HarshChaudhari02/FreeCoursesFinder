from django.db import models

class Main_subject(models.Model):

    name = models.CharField(max_length=500)

    @staticmethod
    def get_all_main_subject():
        return Main_subject.objects.all()

    def __str__(self):
        return self.name