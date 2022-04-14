from django.urls import path
from .views import home
from mysite import views

urlpatterns = [
    path('' , home.as_view() , name = 'home' ),
    
    path('download/', views.download ,name='download'),
]