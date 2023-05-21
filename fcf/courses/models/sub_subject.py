from django.db import models
from .main_subject import Main_subject

class Sub_subject(models.Model):

    main_subject = models.ForeignKey(Main_subject, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=500)
    img = models.CharField(max_length=5000, default='', blank=True)
    description = models.CharField(max_length=10000, default='', blank=True)

    @staticmethod
    def get_all_sub_subject():
        return Sub_subject.objects.all()

    @staticmethod
    def get_all_sub_subject_by_ms(name):
        return Sub_subject.objects.get(main_subject=name)

    @staticmethod
    def get_all_subject_by_id(subject_id):
        return Sub_subject.objects.filter(id=subject_id)

    def __str__(self):
        return self.name