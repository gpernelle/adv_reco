from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.adventure_list, name='adventure_list'),
    path('recommended/', views.RecommendedAdventuresView.as_view(), name='recommended-adventures'),

]

