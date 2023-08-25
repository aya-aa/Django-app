from django import forms
from cProfile import label


class InputForm(forms.Form):
	x=forms.IntegerField(label="Enter first Number:")
	y=forms.IntegerField(label="Enter second number")





class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class FileFieldForm(forms.Form):
    file_field = MultipleFileField()


#n7oti el form di fi milaf html
class PrimeForm(forms.Form):
	x=forms.IntegerField(label="Enter Number")



#class MultiFileUploadForm(forms.Form):
 #   files = forms.FileField(widget=forms.ClearableFileInput(attrs={"allow_multiple_selected": True}))

