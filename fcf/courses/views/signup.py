from django.shortcuts import render, redirect
from courses.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        password_again = postData.get('password_again')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)

        error_message = None
        if (not customer.first_name):
            error_message = "First name Required !!"
        elif len(customer.first_name) < 1:
            error_message = "First name must be more than one character"
        if (not customer.last_name):
            error_message = "Last name Required !!"
        elif len(customer.last_name) < 1:
            error_message = "Last name must be more than one character"
        elif not customer.phone:
            error_message = "Phone number is required"
        elif len(customer.phone) < 10:
            error_message = "Phone number Invalid"
        elif not customer.password:
            error_message = "Password is required"
        elif len(customer.password) < 6:
            error_message = "Password should be more than 6 characters"
        elif not password_again:
            error_message = "Please confirm password"
        elif not customer.password == password_again:
            error_message = "Password does not match"

        isexists = customer.isexists()
        if isexists:
            error_message = "Email already exists"

        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('login')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)
