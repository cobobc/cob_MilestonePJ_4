from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_beats, name='beats'),
    path('<int:beat_id>/', views.beat_detail, name='beat_detail'),
    path('add/', views.add_beat, name='add_beat'),
]