from django.views import View
from django.shortcuts import render, redirect, HttpResponse
from courses.models.main_subject import Main_subject
from courses.models.sub_subject import Sub_subject
from courses.models.institute import Institute
from courses.models.university import University
from courses.models.provider import Provider
from courses.models.sub_subject import Sub_subject
from courses.models.course import Course
from django.core.paginator import Paginator
from courses.views import search_scrap
from django.http import JsonResponse

class Search(View):
    def get(self, request):
        data = {}
        details_data = {}
        courses = None

        institute_id = request.GET.get('institute')
        university_id = request.GET.get('university')
        subject_id = request.GET.get('subject')
        provider_id = request.GET.get('provider')

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

        course_id = request.GET.get('course')
        if course_id:
            course_data = Course.get_all_course_details_by_id(course_id)
            related_data = Course.get_all_courses_by_sub_id(course_data.sub_subject.id)
            return render(request, 'course_details.html', {'course_details': course_data, 'related_data': related_data})

        str_query = ''
        if institute_id:
            courses = Course.get_all_courses_by_insti_id(institute_id).order_by('id')
            query_name = Institute.get_all_institute_by_id(institute_id)
            str_query = 'institute'
        elif university_id:
            courses = Course.get_all_courses_by_uni_id(university_id).order_by('id')
            query_name = University.get_all_university_by_id(university_id)
            str_query = 'university'
        elif subject_id:
            courses = Course.get_all_courses_by_sub_id(subject_id).order_by('id')
            query_name = Sub_subject.get_all_subject_by_id(subject_id)
            str_query = 'subject'
        elif provider_id:
            courses = Course.get_all_courses_by_prov_id(provider_id).order_by('id')
            query_name = Provider.get_all_provider_by_id(provider_id)
            str_query = 'provider'

        if courses:
            length = 'Total ' + str(len(courses)) + ' courses'
            paginator = Paginator(courses, 15)
            page_no = request.GET.get('page')
            course = paginator.get_page(page_no)

            details_data['courses'] = course
            details_data['query_name'] = query_name
            details_data['length'] = length
            details_data['str_query'] = str_query
            return render(request, 'details.html', details_data)

        courses = None
        query = ''
        query = request.GET.get('query')
        print(query)
        course = None


        if query:
            if len(query)>78:
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
        else:
            if query:
                course_details, counter, img = search_scrap.search_google(query)
                if counter > 0:
                    searchResultsFound = True
                    print("hello")
                    #return JsonResponse({'course_details': course_details, 'counter':counter, 'img':img, 'query': query})
                    return render(request, 'search.html', {'course_details': course_details, 'counter':counter, 'img':img, 'query': query})
        print(query)
        return render(request,'search.html',{'courses':course,'counter':counter, 'query':query})
