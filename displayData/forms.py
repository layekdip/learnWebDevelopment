from django import forms


class DataSourceNameForm(forms.Form):
    data_file_to_be_used = forms.CharField(max_length=100)

