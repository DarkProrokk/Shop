from django import forms


class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 3:
            raise forms.ValidationError("Имя должно содержать не менее 3 символов")
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError("Пароль должен содержать не менее 8 символов")
        if password.isdigit():
            raise forms.ValidationError("Пароль должен содержать буквы")
        if password.isalpha():
            raise forms.ValidationError("Пароль должен содержать цифры")
        return password
