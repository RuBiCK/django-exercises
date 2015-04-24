from django import forms
from tweets.models import User

class RegisterForm(forms.Form):
    nick = forms.CharField(max_length=20,label='Nick')
    email = forms.EmailField(required=True, label='E-mail')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    passwordRep = forms.CharField(widget=forms.PasswordInput, label='RepitePassword')
    def clean_password(self):
        if len(self.cleaned_data['password']) < 6:
            raise forms.ValidationError("Password muy corto. Debe ser superior a 6 caracteres")
        return self.cleaned_data['password']
    def clean(self):
        cleaned_data = self.cleaned_data
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("passwordRep")
        if password1 != password2:
            raise forms.ValidationError("Los passwords deben coincidir.")
        return cleaned_data

    def clean_nick(self):
        cleaned_data = self.cleaned_data
        nickform = cleaned_data.get("nick")
        if User.objects.filter(nick=nickform):
            raise forms.ValidationError("El usuario existen")
        return cleaned_data

