from django import forms
import re
from .models import Tracks

class TrackForm(forms.ModelForm):
    class Meta:
        model = Tracks
        fields = ['track_name', 'track_duration', 'track_supervisor', 'track_start_date', 'track_end_date']
        widgets = {
            "track_name": forms.TextInput(attrs={'placeholder': 'Enter track name'}),
            "track_duration": forms.TextInput(attrs={'placeholder': 'Enter track duration'}),
            "track_supervisor": forms.TextInput(attrs={'placeholder': 'Enter track supervisor'}),
            "track_start_date": forms.DateInput(attrs={'type': 'date', 'placeholder': 'MM/DD/YYYY'}),
            "track_end_date": forms.DateInput(attrs={'type': 'date', 'placeholder': 'MM/DD/YYYY'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        track_name = cleaned_data.get('track_name')
        if track_name:
            if not re.match(r'^[A-Za-z\s]+$', track_name):
                raise forms.ValidationError("Track name must contain only letters and spaces.")
        else:
            raise forms.ValidationError("Track name is required.")

        track_start_date = cleaned_data.get('track_start_date')
        track_end_date = cleaned_data.get('track_end_date')

        if track_start_date and track_end_date:
            if track_end_date < track_start_date:
                raise forms.ValidationError("End date must be after start date.")
                
        return cleaned_data
