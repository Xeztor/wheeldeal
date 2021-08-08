from django.shortcuts import render
from django.views.generic import TemplateView

from wheeldeal.profiles.models import UserProfile


class IndexView(TemplateView):
    template_name = 'common/index.html'


class AboutUsView(TemplateView):
    template_name = 'common/about_us.html'


class ContactsView(TemplateView):
    template_name = 'common/contacts.html'
