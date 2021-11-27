from django import forms
from django.forms.widgets import Widget

# iterable
StaffDept =(
    ("Mca", "Mca"),
    ("Bca", "Bca"),
    ("UG_Lab", "UG Lab"),
    ("PG_Lab", "PG Lab"),
    ("Library", "Library"),
    ("Hostel", "Hostel"),
    ("Office", "Office")
)

StaffYear =(
    ("1", "1St year"),
    ("2", "2nd year"),
    ("3", "3rd year"),
    ("4", "4th year")   
)

class StaffLogin(forms.Form):
    Department = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-select select2-hidden-accessible','name':'staffdept'}),choices=StaffDept)
    Year = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-select select2-hidden-accessible','name':'staffdept'}),choices=StaffYear)
    Password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg','name':'staffpassword','id':'password','placeholder':'Enter your password','type':'password'}))

class StudentLogin(forms.Form):
    Register_Number = forms.CharField(widget=forms.TextInput(attrs={'name':'studentregno', 'required':'required', 'type':'text', 'class':'form-control', 'id':'studentregno', 'placeholder':'Enter your Register number'}))
    Password = forms.CharField(widget=forms.TextInput(attrs={'type':'date', 'class':'form-control form-control-lg', 'id':'password', 'placeholder':'Enter your passcode'}))

class AdminLogin(forms.Form):
    Username = forms.CharField(widget=forms.TextInput(attrs={'name':'studentregno', 'required':'required', 'type':'text', 'class':'form-control', 'id':'studentregno', 'placeholder':'Enter your Register number'}))
    Password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg','name':'staffpassword','id':'password','placeholder':'Enter your password','type':'password'}))
