from django import forms
from .models import Hospital

class Hospitalform(forms.ModelForm):
	class Meta:
			model = Hospital
			fields = '__all__'