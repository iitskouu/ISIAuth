from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, CreateView

from dashboard.forms import ClubSignUpForm, DeanSignUpForm
from dashboard.models import User


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_club:
            return HttpResponse('hi club')
        else:
            return HttpResponse('hi dean')
    return render(request, 'home.html')


class ClubSignUpView(CreateView):
    model = User
    form_class = ClubSignUpForm
    template_name = 'registration/signup_form.html'


class DeanSignUpView(CreateView):
    model = User
    form_class = DeanSignUpForm
    template_name = 'registration/signup_form.html'
