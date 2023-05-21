from django.db import models
from .university import University
from .provider import Provider
from .institute import Institute
from .language import Language
from .certificate import Certificate
from .main_subject import Main_subject
from .sub_subject import Sub_subject

class Course(models.Model):

    url = models.CharField(max_length=500)
    img = models.CharField(max_length=5000, default='')
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500, default='', blank=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, default=' ')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, default=' ')
    institution = models.ForeignKey(Institute, on_delete=models.CASCADE, default=' ')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=' ')
    time = models.CharField(max_length=100, blank=True)
    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE, default=' ')
    main_subject = models.ForeignKey(Main_subject, on_delete=models.CASCADE, default=' ')
    sub_subject =models.ForeignKey(Sub_subject, on_delete=models.CASCADE, default=' ')
    rating = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=10000, blank=True)
    sub_title = models.CharField(max_length=5000, default='', blank=True)


    @staticmethod
    def get_all_courses_by_insti_id(institute_id):
        try:
            return Course.objects.filter(institution=institute_id)
        except:
            return "Error"

    @staticmethod
    def get_all_courses_by_uni_id(university_id):
        try:
            return Course.objects.filter(university=university_id)
        except:
            return "Error"

    @staticmethod
    def get_all_courses_by_sub_id(subject_id):
        try:
            return Course.objects.filter(sub_subject=subject_id)
        except:
            return "Error"

    @staticmethod
    def get_all_courses_by_prov_id(provider_id):
        try:
            return Course.objects.filter(provider=provider_id)
        except:
            return "Error"

    @staticmethod
    def get_all_course_details_by_id(course_id):
        try:
            return Course.objects.get(id=course_id)
        except:
            return "Error"

    @staticmethod
    def get_all_courses():
        try:
            return Course.objects.all()
        except:
            return "Error"