from django import forms
from.models import post,category,comment


choices = category.objects.all().values_list('name','name')

choicelist = []

for item in choices:
    choicelist.append(item)

class postform(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title','title_tag','author','category','body','image']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choicelist, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
class  Edit(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title','title_tag','body']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['name','body']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }