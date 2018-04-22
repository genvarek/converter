from django import forms
from blog.models import Query


class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ('link',)