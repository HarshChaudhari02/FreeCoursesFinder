from django.contrib import admin
from .models.course import Course
from .models.certificate import Certificate
from .models.main_subject import Main_subject
from .models.sub_subject import Sub_subject
from .models.university import University
from .models.institute import Institute
from .models.provider import Provider
from .models.language import Language
from .models.customer import Customer
from .models.contact import Contact
# Register your models here.


class AdminCourse(admin.ModelAdmin):
    list_display = ['title', 'provider']

class AdminDisplay(admin.ModelAdmin):
    list_display = ['name']



# Register your models here.
admin.site.register(Course, AdminCourse)
admin.site.register(Certificate, AdminDisplay)
admin.site.register(Main_subject, AdminDisplay)
admin.site.register(Sub_subject, AdminDisplay)
admin.site.register(University, AdminDisplay)
admin.site.register(Institute, AdminDisplay)
admin.site.register(Provider, AdminDisplay)
admin.site.register(Language, AdminDisplay)
admin.site.register(Customer)
admin.site.register(Contact)