from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import Textarea, Select, TextInput, CheckboxInput
from news.models import News
import re

class AddNewsForm(forms.ModelForm):
    # title = forms.CharField()
    class Meta:
        model = News
        fields = ["caption", "text", "is_published", 'category']
        widgets = {'caption': TextInput(attrs={'class': "form-control", 'cols': 40, 'rows': 1}),
                   'text': Textarea(attrs={'class': "form-control", 'cols': 40, 'rows': 10}),
                   'category': Select(attrs={'class': "form-select"}),
                   'is_published': CheckboxInput(attrs={'class': "form-check-input"})

                   }
        labels = {
            'text': ('Текст новости'),
        }

    # def clean_caption(self):
    #     caption = self.cleaned_data["caption"]
    #     if re.match(r"\d", caption):
    #         raise ValidationError("Назване не должно начинать с цифр!!!")

class AddUserForm(forms.ModelForm):
    photo = forms.ImageField(required=False)
    password = forms.CharField()
    password2 = forms.CharField()
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "first_name", 'last_name']
        # widgets = {'caption': TextInput(attrs={'class': "form-control", 'cols': 40, 'rows': 1}),
        #            'text': Textarea(attrs={'class': "form-control", 'cols': 40, 'rows': 10}),
        #            'category': Select(attrs={'class': "form-select"}),
        #            'is_published': CheckboxInput(attrs={'class': "form-check-input"})

        #            }
        # labels = {
        #     'text': ('Текст новости'),
        # }

    def save(self, commit=True):
        if self.cleaned_data["password"] == self.cleaned_data["password2"]:
           user = super().save()
        else:
            raise forms.ValidationError("Пароли не совпадают")
        return      user