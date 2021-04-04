from django.urls import path, include
from . import views
# from django.contrib.auth import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup', views.SignUpView.as_view(), name="signup"),
]
