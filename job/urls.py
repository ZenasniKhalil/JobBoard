from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home' ),
    path('job_detail/<pk>/', views.job_detail , name='job_detail' ),
    path('job_listing/', views.job_listing, name='job_listing'),
]