from django import forms 
from .models import Task

class TaskForm(forms.ModelForm):    

    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter task title',
                'class': 'form-control'  # optional for styling
            }),

            'description': forms.Textarea(attrs={
                'placeholder': 'Add a description...',
                'class': 'form-control',  # optional
                'rows': 4  # optional
            }),

            "due_datetime": forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        
        }

        #alternate
        #fields = ['title', 'description', 'completed']





