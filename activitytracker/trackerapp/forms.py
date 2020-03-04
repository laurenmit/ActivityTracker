from django import forms
from .models import Activity, Totals

ACTIVITY_CHOICES = [
    ('run', 'Run'),
    ('walk', 'Walk'),
    ('hike', 'Hike'),
    ('swim', 'Swim'),
    ('cycle', 'Cycle'),
    ('other', 'Other')
    ]

class ActivityForm(forms.ModelForm):
     distance_km = forms.DecimalField(max_digits=8,decimal_places=3)
     time_stamp =forms.TimeField(label = 'Activity Time',widget=forms.TimeInput(attrs={'placeholder':'hh:mm:ss'}))
     activity_type = forms.CharField(widget=forms.Select(choices=ACTIVITY_CHOICES))
     date = forms.DateField(label = 'Activity Date',widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD'}))

     def __init__(self, *args, **kwargs):
         super(forms.ModelForm, self).__init__(*args, **kwargs)
         self.fields['distance_km'].label = 'Distance [km]'
         self.fields['time_stamp'].label = 'Time Taken HH:MM:SS'
         self.fields['activity_type'].label = 'Activity Type'
         self.fields['date'].label = 'Date'


     class Meta:
         model = Activity
         fields = (
                     'distance_km',
                     'time_stamp',
                     'activity_type',
                     'date'
                 )
