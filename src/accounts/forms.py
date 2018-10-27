from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class LoginForm(forms.Form):
    username=forms.CharField(required=True)
    password=forms.CharField(widget=forms.PasswordInput,required=True)


    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password = password)
            if not user:
                raise forms.ValidationError('user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('password does not match')
            if not user.is_active:
                raise forms.ValidationError('user is not active')
        return super(LoginForm, self).clean(*args, **kwargs)

class SignUpForm(forms.ModelForm):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput,required=True)

    class Meta:

            model=User
            fields=["username","password",
                    ]


