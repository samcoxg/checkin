from django.urls import path, include
from . import views

app_name = 'main'


urlpatterns = [
path('', views.home, name='home'),
path('milkfeedings/', views.MilkFeedingListView.as_view(), name='milkfeedings-list'),
path('addmilkfeeding/', views.MilkFeedingCreateView.as_view(), name='milkfeedings-create'),
path('deletemilkfeeding/<pk>', views.MilkFeedingDeleteView.as_view(), name='milkfeedings-delete')


]