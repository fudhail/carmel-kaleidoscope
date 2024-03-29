from django import forms
import re
from django.forms import ModelForm
from blog.models import Post
from tinymce.widgets import TinyMCE

class ContactForm(forms.Form):

    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'name-field'}))
    email = forms.EmailField(required=False)
    message = forms.CharField(max_length=500, widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']

        if email == '':
            #raise forms.ValidationError("Email or Phone 1 should be field", code='invalid')
            self.add_error("Email should be field")

    # def clean_password(self):
    #     password = self.cleaned_data['password']
    #     r = re.search('[A-Z][a-z][0-9]', password)

    #     if not r:
    #         raise forms.ValidationError("1 Upper, 1Lower, 1Special 1Num", code="upper")
    #     else:
    #         return password


class PostForm(ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    author = forms.CharField(disabled=True)
    pdf_file_extra = forms.FileField(required=False)

    class Meta:
        model = Post
        fields = ['title', 'student', 'content', 'status', 'category', 'subcategory', 'grade', 'thumbnail', 'files', 'video_or_not', 'pdf', 'pdf_file_extra']
