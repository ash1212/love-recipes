from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

User = get_user_model()


class RegisterForm(UserCreationForm):
    name = forms.CharField(label="Name", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'John Doe', }))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'john@loverecipes.com', }))

    class Meta:
        model = User
        fields = ('name', 'email', 'password1', 'password2')

    # def clean_password(self):
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')
    #     if password1 is not password2:
    #         raise forms.ValidationError("password do not match")
    #     return password2
    #
    # def save(self, commit=True):
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.set_password(self.cleaned_data['password1'])
    #     if commit:
    #         user.save()
    #     return user


class UserLoginForm(forms.Form):
    query = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        query = self.cleaned_data.get('query')
        password = self.cleaned_data.get('password')
        user_qs_final = User.objects.filter(Q(email__iexact=query)).distinct()
        if not user_qs_final.exists() and user_qs_final.count != 1:
            raise forms.ValidationError("Invalid credentials - User does not exist")
        user_obj = user_qs_final.first()
        if not user_obj.check_password(password):
            raise forms.ValidationError("Incorrect credentials")
        self.cleaned_data["user_obj"] = user_obj
        return super(UserLoginForm, self).clean(*args, **kwargs)
