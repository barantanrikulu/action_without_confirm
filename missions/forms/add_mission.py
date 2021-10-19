from django import forms
from django.forms import fields
from missions.models import Mission


class AddMissionModelForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'placeholder': 'Add new task...'}))

    class Meta:
        model = Mission
        fields = ("title",)
