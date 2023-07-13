from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "index.html"


class ContactPageView(TemplateView):
    template_name = "contact.html"


class AboutUsPageView(TemplateView):
    template_name = "about-us.html"


class GalleryPageView(TemplateView):
    template_name = "gallery.html"


class ServicePageView(TemplateView):
    template_name = "services.html"
