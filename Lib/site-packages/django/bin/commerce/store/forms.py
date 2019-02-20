from django import forms
from.models import *
from django.forms.utils import ErrorList

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"


class ParagraphErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<p class="small error">%s</p>' % e for e in self])

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'




