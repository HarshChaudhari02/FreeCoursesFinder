from django.views import View
from django.shortcuts import render, redirect


class Details(View):
    def get(self, request):
        return render(request, 'details.html')
