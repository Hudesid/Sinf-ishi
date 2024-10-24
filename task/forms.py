from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'due_date', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'due_date': forms.TimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }