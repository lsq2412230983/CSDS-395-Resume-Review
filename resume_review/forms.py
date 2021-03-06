from django import forms
from django.contrib.auth import password_validation, authenticate
from django.contrib.auth.models import User
from django.forms import ValidationError, Select

from resume_review import source_api


class RegisterForm(forms.Form):
    username = forms.CharField(required=True, label='Username')
    email = forms.EmailField(required=True)
    password1 = forms.CharField(required=True, label='Password')
    password2 = forms.CharField(required=True, label='Verify password')

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@case.edu'):
            raise ValidationError('Domain of email is not valid')
        return email

    def clean(self):
        password = self.cleaned_data.get('password1')
        re_password = self.cleaned_data.get('password2')
        username = self.cleaned_data.get('username')

        users = User.objects.filter(username=username)
        if len(users) > 0:
            self.add_error('username', "Username has existed")

        if not password == re_password:
            self.add_error('password2', "Passwords must match")

        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Username')
    password = forms.CharField(required=True, label='Password')

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user and username and password:
            users = User.objects.filter(username=username)
            if len(users) == 0:
                self.add_error('username', "Please enter the valid username.")
            else:
                self.add_error('password', "Please enter the valid password.")
        return self.cleaned_data


class UserProfileForm(forms.Form):
    first_name = forms.CharField(required=True, label='First Name', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}))
    last_name = forms.CharField(required=True, label='Last Name', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}))
    avatar = forms.ImageField(required=False, label='Avatar')
    phone_number = forms.CharField(required=True, label='Phone Number', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}))
    MAJOR_CHOICES = source_api.get_major_list()
    major = forms.ChoiceField(choices=MAJOR_CHOICES, required=True, label='Major',
                              widget=Select(attrs={"class": "form-select"}), initial='Accounting')
    self_intro = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Enter your self introduction'}))
    price = forms.IntegerField(required=False)

    FRESHMEN = 'Freshmen'
    SOPHOMORE = 'Sophomore'
    JUNIOR = 'Junior'
    SENIOR = 'Senior'
    GRADUATE = 'Graduate'

    ACADEMIC_STANDING_CHOICES = [
        (FRESHMEN, 'Freshmen'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]

    DELIVERY_TIME_CHOICES = [
        ('One week', 'One week'),
        ('Two weeks', 'Two weeks'),
        ('Three weeks', 'Three weeks'),
        ('Four weeks or more', 'Four weeks or more'),
    ]

    academic_standing = forms.ChoiceField(choices=ACADEMIC_STANDING_CHOICES, required=True, initial='Freshman', label='Academic Standing',
                                          widget=Select(attrs={"class": "form-select"}))

    delivery_time = forms.ChoiceField(choices=DELIVERY_TIME_CHOICES, required=True, initial='One week', label='Delivery Time',
                                          widget=Select(attrs={"class": "form-select"}))


class SearchForm(forms.Form):
    MAJOR_CHOICES = source_api.get_major_list()
    MAJOR_CHOICES.insert(0, ('All', 'All'))

    ALL = 'All'
    FRESHMEN = 'Freshmen'
    SOPHOMORE = 'Sophomore'
    JUNIOR = 'Junior'
    SENIOR = 'Senior'
    GRADUATE = 'Graduate'
    ACADEMIC_STANDING_CHOICES = [
        (ALL, 'All'),
        (FRESHMEN, 'Freshmen'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]
    PRICE_CHOICE = [
        ('All', 'All'),
        ('1', '<20'),
        ('2', '20-50'),
        ('3', '50-100'),
        ('4', '>100'),
    ]

    name = forms.CharField(required=False, label='Name', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the name'}))
    # three choices to filter
    major = forms.ChoiceField(choices=MAJOR_CHOICES, required=True, label='Major',
                              widget=Select(attrs={"class": "form-select"}), initial='All')
    academic_standing = forms.ChoiceField(choices=ACADEMIC_STANDING_CHOICES, required=True, label='Standing',
                                          widget=Select(attrs={"class": "form-select"}), initial='All')
    price = forms.ChoiceField(choices=PRICE_CHOICE, required=True, label='Price',
                              widget=Select(attrs={"class": "form-select"}), initial='All')

class OrderDetailForm(forms.Form):
    resume = forms.FileField()