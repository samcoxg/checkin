from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import *

# Create your views here.
def home(req):
    return render(req, 'main/index.html')


class MilkFeedingListView(ListView):
    model = MilkFeeding


class MilkFeedingCreateView(CreateView):
    model = MilkFeeding
    fields = ['total_amount', 'formula_type', 'formula_percent', 'breast_milk_percent']