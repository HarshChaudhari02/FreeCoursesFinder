from django.db import models

class University(models.Model):

    name = models.CharField(max_length=500)
    img = models.CharField(max_length=5000, default='', blank=True)
    description = models.CharField(max_length=10000, default='', blank=True)

    @staticmethod
    def get_all_university():
        return University.objects.all()

    @staticmethod
    def get_all_university_by_id(university_id):
        return University.objects.filter(id=university_id)

    def __str__(self):
        return self.name