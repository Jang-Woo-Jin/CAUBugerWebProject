from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from .models import User, Menu, Seat, Order, Notice
from .forms import SignupForm, SearchPWForm, ChangePWForm
from django.contrib.auth.models import User
from django.contrib.auth import login

#Main Page
def index(request):
    template = loader.get_template('mycontact/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
    
#Introduction Page
def introduction(request):
    template = loader.get_template('mycontact/introduction.html')
    menus = Menu.objects.order_by('menuName')
    menuTemplate = list()
    row = list()
    count = 0
    for i in range(0,23):
        if count == 0:
            row = list()
            row.append(menus[i])
        elif count < 5:
            row.append(menus[i])
        count = count + 1
        if count == 5:
            menuTemplate.append(row)
            count = 0
    menuTemplate.append(row)
    context = {
        'menus' : menuTemplate
    }
    return HttpResponse(template.render(context, request))

#Order Page
def order(request):
    template = loader.get_template('mycontact/order.html')
    orders = Order.objects.order_by('orderId')
    context = {
        'orders' : orders
    }
    return HttpResponse(template.render(context, request))

#Seat Page
def seats(request):
    template = loader.get_template('mycontact/seats.html')
    seats = Seat.objects.order_by('seatNo')
    seatsTemplate = list()
    row = list()
    count = 0 
    for i in range(0,56):
        if count == 0:
            row = list()
            row.append(seats[i])
        elif count < 8:
            row.append(seats[i])
        count = count + 1
        if count == 8:
            seatsTemplate.append(row)
            count = 0
    context = {
        'seats' : seatsTemplate
    }
    return HttpResponse(template.render(context, request))

#Notice Page
def notice(request):
    template = loader.get_template('mycontact/notice.html')
    contacts = Notice.objects.order_by('pk')
    context = {
        'contacts' : contacts
    }
    return HttpResponse(template.render(context, request))

#Signup Page
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('index')
    else:
        form = SignupForm()

    template = loader.get_template('registration/signup.html')
    context = {
        'form' : form
    }
    return HttpResponse(template.render(context, request))

def changepw(request):
    user = request.user
    isError = False
    form = PasswordChangeForm(user, request.POST)
    if request.method == 'POST':
        if form.is_valid():
            changed_user = form.save()
            update_session_auth_hash(request, changed_user)  # Important!
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
            isError = True
            return render(request, 'registration/changepw.html', {'user' : user, 'form': form, "isError" : isError})
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'registration/changepw.html', {'user' : user, 'form': form})