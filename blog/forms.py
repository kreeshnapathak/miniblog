from .models import Post, BlogComment
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.models import User
from django.forms import fields, widgets
from django.utils.timezone import now


class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='Password', widget=forms.PasswordInput( attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password(re-enter)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        
        model=User
        fields=['username','first_name','last_name','email']
        labels={'first_name':'First Name','last_name':'Last Name', 'email':"Email"}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.TextInput(attrs={'class':'form-control'}),
        'password1':forms.TextInput(attrs={'class':'form-control'})}


class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,
    'class':'form-control'}))   
    password=forms.CharField(label=_("password"),strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete':'current-password',
    'class':'form-control'}))      


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','desc','author','feild','datetime']
        labels={'title':'Title','author':'Author','feild':'Feild','datetime':'Date','desc':'Description'}
        widgets={'title':forms.TextInput(attrs={'class':"form-control"}),
        'author':forms.TextInput(attrs={'class':"form-control"}),
        'feild':forms.TextInput(attrs={'class':"form-control"}),
        'desc':forms.Textarea(attrs={'class':"form-control"})
        
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=BlogComment
        fields=['name','body']
        labels={'Name':'Full Name','body':'Your Comments:'}
        widgets={'name':forms.TextInput(attrs={'class':"form-control"}),
        'body':forms.TextInput(attrs={'class':"form-control"})}
