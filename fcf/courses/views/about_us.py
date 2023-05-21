from django.views import View
from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from courses.models.contact import Contact
from django.shortcuts import render,redirect
from courses.models.main_subject import Main_subject
from courses.models.sub_subject import Sub_subject
from courses.models.institute import Institute
from courses.models.university import University
from courses.models.provider import Provider
from courses.models.sub_subject import Sub_subject
from courses.models.course import Course
from django.core.paginator import Paginator
from courses.views import search_scrap

class About_us(View):
    def get(self, request):
        courses = None
        query = ''
        query = request.GET.get('query')
        print(query)
        course = None

        if query:
            if len(query) > 78:
                courses = []
            else:
                courses = Course.objects.filter(title__icontains=query)

        searchResultsFound = False
        counter = 0
        if courses:
            paginator = Paginator(courses, 15)
            page_no = request.GET.get('page')
            course = paginator.get_page(page_no)
            searchResultsFound = True
            return render(request, 'search.html', {'courses': course, 'counter': counter, 'query': query})
        else:
            if query:
                course_details, counter, img = search_scrap.search_google(query)
                if counter > 0:
                    searchResultsFound = True
                    print("hello")
                    # return JsonResponse({'course_details': course_details, 'counter':counter, 'img':img, 'query': query})
                    return render(request, 'search.html',
                                  {'course_details': course_details, 'counter': counter, 'img': img, 'query': query})
                else:
                    return render(request, 'search.html', {'courses': course, 'counter': counter, 'query': query})

        return render(request, 'about_us.html')