from django import forms

class MyFileUploadForm(forms.Form):
    files=forms.FileField(widget=forms.FileInput(attrs={'class':'form-control' }))