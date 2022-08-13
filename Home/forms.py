from django.contrib.auth.forms import UserCreationForm
from .models import User

from .models import Idcard
from django import forms 

CHOICES = [('1', '-----'), ('2', 'Kathmandu'),
           ('3', 'Bhaktapur'), ('4', 'Lalitpur'), ('5', 'Chitwan')]
gen = [('1', '-----'), ('2', 'Female'),
       ('3', 'Male'), ('4', 'Others')]
stat = [('1', '-------'), ('2', 'Single'),
        ('3', 'Divorce'),('4','Married')]
Edu_level = [('1', '------'), ('2', 'Slc'),('3','Plus 2'),
             ('4', 'Bacehlors'), ('5', 'Masters'), ('6', 'PHDs'), ('7', 'Uneducated')]
prof = [('1', '-----'), ('2', 'Service'), ('3', 'Doctor'), ('4', 'Framer'),
        ('5', 'Teacher'), ('6', 'Social Worker'), ('7', 'Lawyer'), ('8', 'Businessman'), ('9', 'Others')]
CasteChoice = [('1', '----'), ('2', 'Chettri'), ('3', 'Brahmin'), ('4', 'Newar'),
               ('5', 'Thakuri'), ('6', 'Others')]
Reli = [('1', '------'), ('2', 'Hindu'), ('3', 'Bouddha'), ('4', 'Islam'),
        ('5', 'Christian'), ('6', 'Others')]


class card(forms.ModelForm):
    firstname =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','Placeholder':'Enter Firstname'}))
    middlename =forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control my-2','Placeholder':'Enter midlename'}))
    lastname =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','Placeholder':'Enter lastname'}))
    dob = forms.DateField(widget=forms.NumberInput(attrs={'class': 'form-control my-2', 'type': 'date','Placeholder': 'Enter Date'}))
    birthplace = forms.ChoiceField(choices=CHOICES, widget=forms.Select(
        attrs={'class': 'form-control my-2', 'Placeholder': 'Choose Birthplace'}))
    citizenship_no = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control my-2', 'Placeholder': 'Enter Citizenship Number'}))
    issue_zone = forms.ChoiceField(label='Zone', choices=CHOICES,widget=forms.Select(
        attrs={'class': 'form-control my-2', 'Placeholder': 'enter zone'}))
    # issue_date = forms.DateField(widget=forms.DateInput(
    #     attrs={'class': 'form-control my-2', 'Placeholder': 'enter issue_date'}))
    
    gender = forms.ChoiceField(label='Gender',  choices=gen, widget=forms.Select(
        attrs={'class': 'form-control my-2', 'Placeholder': 'Choose gender'}))
    
    marital_status = forms.ChoiceField(choices=stat ,widget=forms.Select(
        attrs={'class': 'form-control my-2', 'Placeholder': 'Choose Marital State'}))
    
    education = forms.ChoiceField(choices=Edu_level,widget=forms.Select(
        attrs={'class': 'form-control my-2', 'Placeholder': 'Choose Education level'}))
    
    profession = forms.ChoiceField(choices=prof,widget=forms.Select(
        attrs={'class': 'form-control my-2', 'Placeholder': 'Choose Profession'}))
    
    caste = forms.ChoiceField(choices=CasteChoice,widget=forms.Select(
        attrs={'class': 'form-control my-2', 'Placeholder': 'Choose Caste'}))
    
    religion= forms.ChoiceField(choices=Reli, widget=forms.Select(
        attrs={'class': 'form-control my-2', 'Placeholder': 'Choose Caste'}))
    
    class Meta:
        model= Idcard
        fields=['firstname','middlename','lastname','dob','birthplace','citizenship_no','issue_zone','gender','marital_status','education','profession','caste','religion']
        

class CustomUserForm(UserCreationForm):
    username= forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control my-2','placeholder':'Enter Username'}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control my-2', 'placeholder': 'Enter Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control my-2', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control my-2', 'placeholder': 'Confirm Password'}))
    class Meta:
        model= User
        fields =['username','email','password1','password2']