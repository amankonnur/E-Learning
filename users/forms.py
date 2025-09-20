from .models import PersonDetails
from django import forms


class userForm(forms.ModelForm):
    class Meta:
        model = PersonDetails
        fields = ['username', 'email', 'designation', 'password']
