from django import forms
from .models import TraineeProfile, Tracks

class TraineeForm(forms.ModelForm):
    class Meta:
        model = TraineeProfile
        fields = ['trainee_first_name', 'trainee_last_name', 'trainee_email', 'trainee_phone', 'trainee_address', 'trainee_track']
        widgets = {
            'trainee_first_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Trainee First Name"}),
            'trainee_last_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Trainee Last Name"}),
            'trainee_email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter Trainee Email"}),
            'trainee_phone': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Trainee Phone Number"}),
            'trainee_address': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Trainee Address"}),
            'trainee_track': forms.Select(attrs={"class": "form-control"})
        }
