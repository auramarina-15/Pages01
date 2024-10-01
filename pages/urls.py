
from django.urls import path
from pages.views import HomePageView,AboutPageView

urlpatterns = [
    path("", HomePageView.as_view()),
    path("about/",AboutPageView.as_view(),name="about"),
]



