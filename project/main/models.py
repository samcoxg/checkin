from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class BaseModel(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='create')
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='update')
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)


class MilkFeeding(BaseModel):
    ate_at = models.TimeField(null=False, blank=False)
    total_amount = models.DecimalField(null=False, blank=False, decimal_places=1, max_digits=5)
    formula_type = models.CharField(null=False, blank=False, default='Kirkland ProCare', max_length=300)
    formula_percent = models.IntegerField(null=False, blank=False, help_text='Enter percentage out of 100.', default=100)


class BM(BaseModel):
    changed_at = models.DateTimeField(null=False, blank=False)
    bm_type = models.CharField(null=False, blank=False, max_length=300, choices=[('normal-poop', 'normal-poop'), ('pee', 'pee'), ('poop&pee', 'poop&pee'), ('diarrhea', 'diarrhea'), ('constipated', 'constipated')])
    amount = models.CharField(null=False, blank=False, max_length=300, choices=[('small', 'small'), ('medium', 'medium'), ('large', 'large')])
    color = models.CharField(null=False, blank=False, max_length=300, choices=[('yellow', 'yellow'), ('brown', 'brown'), ('green', 'green')])


# class FishFeed(BaseModel):
#     feed_time = models.DateTimeField(null=False, blank=False)
#     all_fish_ate = models.BooleanField(null=False, blank=False, default=True)
#     notes = models.CharField(null=False, max_length=300)


class CarMaintenance(BaseModel):
    car = models.CharField(null=False, blank=False, max_length=300, choices=[('blue-camry', 'blue-camry'), ('white-camry', 'white-camry')])
    completed_at = models.DateTimeField(null=False, blank=False)
    maintenance_type = models.CharField(null=False, blank=False, max_length=300, choices=[('gas', 'gas'), ('oil', 'oil'), ('tire', 'tire'), ('maintenance', 'maintenance'), ('repair', 'repair')])
    maintenance_details = models.CharField(null=False, blank=False, max_length=300)
    notes = models.CharField(null=False, blank=False, max_length=300)

