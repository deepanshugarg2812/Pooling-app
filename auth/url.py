from django.urls import path,include
from auth import views

urlpatterns = [
    path('',views.Login.as_view()),
    path('',include('main.urls')),
]