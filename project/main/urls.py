from django.urls import path, include
from . import views

app_name = 'main'


urlpatterns = [
path('', views.home, name='home'),
path('milkfeedings/', views.MilkFeedingListView.as_view()),
path('addmilkfeeding/', views.MilkFeedingCreateView.as_view())
]