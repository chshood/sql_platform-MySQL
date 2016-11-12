# -*- coding: utf-8 -*-
from django import forms
from captcha.fields import CaptchaField
from django.contrib.admin import widgets
from django.contrib.auth.models import User
class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        max_length=25,
        label="用户名:",
        error_messages={'required': u'请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"用户名",
            }
        ),
    )
    password = forms.CharField(
    required=True,
    max_length=25,
    label="密码:",
    error_messages={'required': u'请输入密码'},
    widget=forms.PasswordInput(
        attrs={
            'placeholder': u"密码",
            }
        ),
    )
    # captcha = CaptchaField(label="输入验证码:",)
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"用户名和密码为必填项")
        else:
            cleaned_data = super(LoginForm, self).clean()


class AddForm (forms.Form):
    a = forms.CharField(widget=forms.Textarea)

class SqlForm (forms.Form):
    a = forms.CharField(widget=forms.Textarea)
    filename = forms.FileField()

class Logquery(forms.Form):
    begin = forms.DateTimeField(label='dateinfo')
    end = forms.DateTimeField()

class Taskquery(forms.Form):
    end = forms.DateTimeField()

class Uploadform(forms.Form):
    filename = forms.FileField()

class Captcha(forms.Form):
    mycaptcha = CaptchaField(label="验证码:",)