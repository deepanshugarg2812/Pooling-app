from django.urls import path,include
from main import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('index/',views.Index.as_view(),name = "index"),
    path('detail/<slug>',login_required(views.Question.as_view()),name = "question"),
]