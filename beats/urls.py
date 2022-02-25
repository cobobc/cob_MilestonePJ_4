from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_beats, name='beats'),
    path('<int:beat_id>/', views.beat_detail, name='beat_detail'),
    path('add/', views.add_beat, name='add_beat'),
    path('edit/<int:beat_id>/', views.edit_beat, name='edit_beat'),
    path('delete/<int:beat_id>/', views.delete_beat, name='delete_beat'),
    path('add_review/<int:beat_id>/', views.add_review, name='add_review'),
    path('edit_review/<beat_id>/<review_id>/',
         views.edit_review, name='edit_review'),
    path('delete_review/<beat_id>/<review_id>/',
         views.delete_review, name='delete_review'),
]
