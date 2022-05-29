from django import forms
from services.models import Subscriber

class Subscribe(forms.ModelForm):
    name = forms.CharField(max_length=264,widget=forms.TextInput({'placeholder':'Name'}))
    email = forms.CharField(max_length=264,widget=forms.TextInput({'placeholder':'Enter your email..'}))
    class Meta:
        model = Subscriber
        fields = ('name', 'email')
