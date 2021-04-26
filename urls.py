from django.urls import path
from . import views

urlpatterns = [
    path('<int:filmid>/', views.film_reviews, name='film-home'),
    path('<int:filmid>/essays', views.film_essays, name='film-essay'),
    path('', views.film_redirect, name='film-redirect'),
]
