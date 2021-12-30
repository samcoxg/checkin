from django.db import models
from django.contrib.auth import User


# Create your models here.

class BaseModel(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='create')
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='update')
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)


class MilkFeeding(BaseModel):
    ate_at = models.DateTimeField(null=False, blank=False)
    total_amount = models.DecimalField(null=False, blank=False, decimal_places=1)
    formula_type = models.CharField(null=False, blank=False, default='Pro Advance - Similac')
    formula_percent = models.IntegerField(null=False, blank=False, help_text='Enter percentage out of 100.', max=100)
    breast_milk_percent = models.IntegerField(null=False, blank=False, help_text='Enter percentage out of 100.', default=0, max=100)


