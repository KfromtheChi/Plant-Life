from django.forms import ModelForm
from .models import Feeding

class Plant_CareForm(ModelForm):
    class Meta:
        model = Plant_Care
        fields = ['date', 'type']