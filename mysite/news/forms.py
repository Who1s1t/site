from django import forms
from django.forms import Textarea, Select, TextInput
from news.models import MyModel


class AddnewsForm(forms.ModelForm):
    # title = forms.CharField()
    class Meta:
        model = MyModel
        fields = ["caption", "text", "is_published", 'category']
        widgets = {'caption': TextInput(attrs={'class': "form-control", 'cols': 40, 'rows': 1}),
                   'text': Textarea(attrs={'class': "form-control", 'cols': 40, 'rows': 10}),
                   'category': Select(attrs={'class': "form-select"})
                   }
