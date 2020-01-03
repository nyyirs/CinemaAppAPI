from django.urls import include, path
from . import views

urlpatterns = [
    path('bagatelle/', views.BagatelleView.as_view()),
]
