from django import forms
from models import analytics, jcanalytics

class orgform(forms.Form):
    choice=[(x.id,str(x.org)) for x in jcanalytics.objects.all().order_by('org')]
    organization = forms.ChoiceField(choice)
