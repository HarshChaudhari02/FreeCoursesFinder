from django.views import View
from django.shortcuts import render, redirect

from courses.models.customer import Customer
from django.contrib.auth.hashers import  check_password

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        customer = Customer.get_customer_by_email(email)
        password = request.POST.get('password')
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['customer_email'] = customer.email
                request.session['customer_fname'] = customer.first_name
                request.session['customer_lname'] = customer.last_name
                request.session['customer_phone'] = customer.phone
                return redirect('homepage')
            else:
                error_message = "Email or Password Invalid"
        else:
            error_message = "Email or Password Invalid"

        return render(request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')