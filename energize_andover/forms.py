from django import forms

class MetasysUploadForm(forms.Form):
    summarize = forms.BooleanField(
        label='Group by day',
        required=False
    )

    metasys_file = forms.FileField(
        label='Select a file'
    )
