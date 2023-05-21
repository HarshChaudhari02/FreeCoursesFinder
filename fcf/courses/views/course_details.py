from django.views import View
from django.shortcuts import render, redirect

class courseDetails(View):
    def get(self, request):
        return render(request, 'course_details.html')