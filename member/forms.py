from django import forms

class UploadFileForm(forms.Form):
    Mem_id = forms.CharField(max_length=200)
    Mem_pwd = forms.CharField(max_length=200)
    Mem_name = forms.CharField(max_length=200)
    Mem_img = forms.ImageField()
