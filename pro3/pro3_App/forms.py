from django import forms
from .models import model_for_form

class example_form(forms.ModelForm):
    class Meta:
        model = model_for_form
        fields="__all__"
        # exclude=('upload_photo',)