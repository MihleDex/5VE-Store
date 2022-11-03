from django import forms
from .models import NewsLetter
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.EmailField(required=True,label="Email")
    class Meta:
        model = User
        fields = ["username","password1","password2"]
    def __init__(self, *args, **kwargs):
        super(RegisterForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control  mb-3 mt-2'
        self.fields['username'].widget.attrs['style']='border-radius:20px;'
        self.fields['password1'].widget.attrs['class']='form-control  mb-3 mt-2'
        self.fields['password1'].widget.attrs['style']='border-radius:20px;'
        self.fields['password2'].widget.attrs['class']='form-control  mb-3 mt-2'
        self.fields['password2'].widget.attrs['style']='border-radius:20px;' 
        self.fields['password1'].help_text=''
        self.fields['username'].help_text=''
        self.fields['password2'].help_text=''

class CustomAuthForm(AuthenticationForm):
    username = forms.EmailField(required=True,label="Email")
    class Meta:
        model = User
        fields = ["email","password"]
    def __init__(self, *args, **kwargs):
        super(CustomAuthForm,self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['class']='form-control  mb-3 mt-2'
        self.fields['password'].widget.attrs['style']='border-radius:20px;'
        self.fields['username'].widget.attrs['style']='border-radius:20px;'
        self.fields['username'].widget.attrs['class']='form-control  mb-3 mt-2' 

class NewsFieldForm(forms.ModelForm):
    email = forms.EmailField(max_length=200,required=False)

    class Meta:
        model = NewsLetter
        fields = ['email',]

    def __init__(self, *args, **kwargs):
        super(NewsFieldForm,self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class']='form-control rounded-5 shadow'
        self.fields['email'].widget.attrs['style']='border-radius:20px;'