from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Shopper_database
from .forms import SignInForm, SignUpForm
# Create your views here.

username = ""


def openSignIn(request):
    template = loader.get_template('sign_in.html')
    global username
    context = {}
    if request.method == 'POST':

        form = SignInForm(request.POST)
        global username_checker

        username_checker = form['username'].value()
        password_checker = form['password'].value()

        username_checker_object = Shopper_database.objects.get(username=username_checker)
        password_from_db = username_checker_object.password

        if password_from_db == password_checker:
            template = loader.get_template('home.html')
            context = {'username': username_checker}
        else:
            template = loader.get_template('sign_in.html')
            context = {}

    return HttpResponse(template.render(context, request))


def openSignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        Shopper_db = Shopper_database(username=form['username'].value(),
                                      password=form['password'].value(),
                                      email=form['email'].value())
        Shopper_db.save()
        template = loader.get_template('sign_in.html')
        context = {}
    else:
        template = loader.get_template('sign_up.html')
        context = {}
    return HttpResponse(template.render(context, request))


def openHome(request):
    template = loader.get_template('home.html')
    context = {'username': username_checker}
    return HttpResponse(template.render(context, request))


def openSeedPackHome(request):
    global total
    context = {'username': username_checker, 'total': total}
    template = loader.get_template('seed_pack_home.html')
    return HttpResponse(template.render(context, request))


def openSeedPackGarden(request):
    context = {'username': username_checker}
    template = loader.get_template('seed_pack_garden.html')
    return HttpResponse(template.render(context, request))


def openPots(request):
    context = {'username': username_checker}
    template = loader.get_template('pots.html')
    return HttpResponse(template.render(context, request))


def openCheckout(request):
    context = {'username': username_checker}
    template = loader.get_template('checkout.html')

    return HttpResponse(template.render(context, request))


def openAboutUs(request):
    context = {'username': username_checker}
    template = loader.get_template('about_us.html')
    return HttpResponse(template.render(context, request))


def openCheckout(request):
    template = loader.get_template('checkout.html')
    context = {'username': username_checker}
    return HttpResponse(template.render(context, request))
