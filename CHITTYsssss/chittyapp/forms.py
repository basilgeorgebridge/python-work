from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from chittyapp.models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms.models import model_to_dict, fields_for_model


# login form

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


# Register Form

class AddMembersForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    idproof = forms.ImageField()

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'age',
            'idproof',
            'username',
            'password1',
            'password2',
            ]

    def save(self, commit=True):
        user = super(AddMembersForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
            UserProfile.objects.create(age=self.cleaned_data["age"],idproof=self.cleaned_data["idproof"],user=user)
        return user

# Edit Members Form

class EditMembersForm(ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    idproof = forms.ImageField()

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'age',
            'idproof',
            'username',
            ]

    def save(self, commit=True):
        user = super(EditMembersForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
            UserProfile.objects.update(age=self.cleaned_data["age"],idproof=self.cleaned_data["idproof"],user=user)
        return user
        



        


    