from django.urls import path
from .views import HomePageView, ContactPageView, \
    ServicePageView, AboutUsPageView, GalleryPageView


urlpatterns = [
    path("index.html", HomePageView.as_view(), name="home"),
    path("", HomePageView.as_view(), name="home1"),
    path("contact.html", ContactPageView.as_view(), name="contact.html"),
    path("about-us.html", AboutUsPageView.as_view(), name="about"),
    path("services.html", ServicePageView.as_view(), name="services"),
    path("gallery.html", GalleryPageView.as_view(), name="gallery"),
]
