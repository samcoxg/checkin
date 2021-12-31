from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy


# Create your views here.
def home(req):
    return render(req, 'main/index.html')


class MilkFeedingListView(ListView):
    model = MilkFeeding


class MilkFeedingCreateView(CreateView):
    model = MilkFeeding
    form_class = MilkFeedingModelForm
    success_url = '/'


class MilkFeedingDeleteView(DeleteView):
    model = MilkFeeding
    success_url = '/milkfeedings'