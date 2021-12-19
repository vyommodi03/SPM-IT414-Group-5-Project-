from django.forms import ModelForm
from .models import OrderItem


class RentdaysForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['days']
