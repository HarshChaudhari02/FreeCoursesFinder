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

class Contact_view(View):
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

        return render(request, 'contact.html')
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('message')

        insti_all = request.GET.get('insti')
        prov_all = request.GET.get('prov')
        uni_all = request.GET.get('uni')
        sub_all = request.GET.get('sub')

        query_name = None
        length = ''
        course_data = None
        related_data = None
        list_data = None
        list_name = ''
        l_name = ''
        query_str = ''

        if insti_all:
            list_data = Institute.get_all_institute().order_by('id')
            list_name = 'Institutes'
            l_name = 'institute'
            query_str = 'insti'
        elif prov_all:
            list_data = Provider.get_all_provider().order_by('id')
            list_name = 'Providers'
            l_name = 'provider'
            query_str = 'prov'
        elif uni_all:
            list_data = University.get_all_university().order_by('id')
            list_name = 'Universities'
            l_name = 'university'
            query_str = 'uni'
        elif sub_all:
            list_data = Sub_subject.get_all_sub_subject().order_by('id')
            list_name = 'Subjects'
            l_name = 'subject'
            query_str = 'sub'

        list_data_p = None
        data_list = {}
        if list_data:
            paginator = Paginator(list_data, 20)
            page_no = request.GET.get('page')
            list_data_p = paginator.get_page(page_no)
            data_list['list_data'] = list_data_p
            data_list['list_name'] = list_name
            data_list['l_name'] = l_name
            data_list['query_str'] = query_str
            return render(request, 'list.html', data_list)

        value = {
            'name': name,
            'email': email,
            'phone': phone,
            'content': content
        }

        contact = Contact(name=name, email=email, phone=phone, content=content)
        error_message = None
        if (not contact.name):
            error_message = "Name Required !!"
        elif len(contact.name) < 1:
            error_message = "Name must be more than one character"
        elif not contact.phone:
            error_message = "Phone number is required"
        elif len(contact.phone) < 10:
            error_message = "Phone number Invalid"
        elif not contact.email:
            error_message = "Email required"
        elif not contact.content:
            error_message = "Message Required"

        if not error_message:
            contact.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'contact.html', data)

