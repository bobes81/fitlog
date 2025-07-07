from django import forms
from .models import WorkoutEntry

class WorkoutEntryForm(forms.ModelForm):
    class Meta:
        model = WorkoutEntry
        fields = ['date', 'workout_type', 'duration_minutes', 'intensity', 'bmi']
