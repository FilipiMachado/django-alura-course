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
        ),
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
        ),
    )

class RegisterForm(forms.Form):
    register_name = forms.CharField(
        label="Username",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: John Doe"
            }
        )
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: johndoe@example.com"
            }
        )
    )
    password_1 = forms.CharField(
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
    password_2 = forms.CharField(
        label="Confirm Password",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirm your password"
            }
        )
    )
    
    def clean_register_name(self):
        name = self.cleaned_data.get("register_name")
        
        if name:
            name = name.strip()
            if " " in name:
                raise forms.ValidationError("You cannot enter blank characters in the username field.")
            else:
                return name
            
    def clean_password_2(self):
        password_1 = self.cleaned_data.get("password_1")
        password_2 = self.cleaned_data.get("password_2")
        
        if password_1 and password_2:
            if password_1 != password_2:
                raise forms.ValidationError("Passwords won't match!")
            else:
                return password_2