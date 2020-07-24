from django import forms

from .models import Picture, Submit


class SubmitForm(forms.Form):
    main_pic = forms.ImageField(label='Основной рисунок')
    new_technique_pic = forms.ImageField(label='Новая техника')
    sketch_pic = forms.ImageField(label='Эскизы (сетка из 10 штук)')

