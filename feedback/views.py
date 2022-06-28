from django.shortcuts import render, redirect
from R_designer.forms import FeedBackForm
from django.views.generic import View
from django.contrib import messages
from R_designer import settings
from feedback import models
from tele.telegramm import send_message


def home(request):
    return render(request, 'home.html')


class FeedBackView(View):
    def post(self, request):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, settings.MY_INFO, 'Заявка создана успешно.')
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = "*ЗАЯВКА С САЙТА*:" + "\n" + "*ИМЯ*: " + str(name) + "\n" + "*ТЕЛЕФОН*: " + str(phone)
            send_message(message)
        else:
            messages.add_message(request, settings.MY_INFO, 'Что-то пошло не так.')
        return redirect("/")

