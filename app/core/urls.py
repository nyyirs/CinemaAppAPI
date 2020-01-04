from django.urls import include, path
from . import views

urlpatterns = [
    path('bagatelle/', views.BagatelleView.as_view()),
    path('trianon/', views.TrianonView.as_view()),
    path('caudan/', views.CaudanView.as_view()),
    path('flacq/', views.FlacqView.as_view()),
]
