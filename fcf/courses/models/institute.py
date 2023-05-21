from django.db import models

class Institute(models.Model):

    name = models.CharField(max_length=500)
    img = models.CharField(max_length=5000, default='', blank=True)
    description = models.CharField(max_length=10000, default='', blank=True)


    @staticmethod
    def get_all_institute():
        return Institute.objects.all()

    @staticmethod
    def get_all_institute_by_id(institute_id):
        return Institute.objects.filter(id=institute_id)

    def __str__(self):
        return self.name