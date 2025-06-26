from django import forms

from users.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email', 'password', 'confirm_password'] #remove phone as it is optional


#Non field validation error


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        # checking for errors in the email field
        email = cleaned_data.get("email")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match.")

        if email and '@' not in email:
            self.add_error("email", "Enter a valid email address.")

        return cleaned_data
