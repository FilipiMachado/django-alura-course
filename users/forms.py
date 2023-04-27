from django import forms

class LoginForm(forms.Form):
    login_name = forms.CharField(
        label="Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: John Doe"
            }
        )
    )
    password = forms.CharField(
        label="Password",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your password"
            }
        )
    )