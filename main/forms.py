from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'phone', 'email', 'note', 'is_archived']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone':  forms.TextInput(attrs={'class': 'form-control'}),
            'email':  forms.TextInput(attrs={'class': 'form-control'}),
            'note':  forms.Textarea(attrs={'class': 'form-control'}),
            'is_archived':  forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }