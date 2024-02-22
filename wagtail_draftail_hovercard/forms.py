from django.forms import forms, fields, widgets


class HovercardForm(forms.Form):
    heading = fields.CharField(required=False)
    text = fields.CharField(required=True, widget=widgets.Textarea)
