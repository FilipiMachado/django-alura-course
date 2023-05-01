from django import forms

from apps.gallery.models import Photograph

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photograph
        exclude = ['published',]
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'caption': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='&d/%m/%Y'),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }