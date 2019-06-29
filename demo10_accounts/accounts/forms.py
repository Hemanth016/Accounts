from django import forms

class FeedBackForm(forms.Form):
     name=forms.CharField()
     password=forms.IntegerField()
     email=forms.EmailField()
     phone_no=forms.IntegerField()
     feedback=forms.CharField(widget=forms.Textarea)


