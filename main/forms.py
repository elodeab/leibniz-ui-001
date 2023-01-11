from django import forms

class SubjectForm(forms.Form):
    subject = forms.CharField(max_length=500)
    
class CodeForm(forms.Form):
    code = forms.CharField(max_length=500)

class TextForm(forms.Form):
    text = forms.CharField(max_length=500)