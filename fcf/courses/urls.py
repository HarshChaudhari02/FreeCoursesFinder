
"""Eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home, login, signup, details, course_details, search, contact, about_us, advance_search
from .views.login import logout
from django.conf.urls.static import static
from fcf import settings


urlpatterns = [
    path('', home.index, name='homepage'),
    path('signup', signup.Signup.as_view(), name= 'signup'),
    path('login', login.Login.as_view(), name= 'login'),
    path('logout', logout, name= 'logout'),
    path('details', details.Details.as_view(), name='details'),
    path('search', search.Search.as_view(), name='search'),
    path('course_details', course_details.courseDetails.as_view(), name='course_details'),
    path('contact', contact.Contact_view.as_view(), name='contact'),
    path('about_us',about_us.About_us.as_view(), name='about_us'),
    path('advance_search', advance_search.advanceSearch.as_view(), name='advance_search')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



