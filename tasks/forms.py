from django import forms
from .models import Task

# class TaskForm(forms.ModelForm):  # ModelForm — это форма, которая автоматически создаётся из модели. Не нужно вручную описывать каждое поле.
#     class Meta:
#         model = Task
#         fields = ['title', 'description']


# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title', 'description']

#     def clean_title(self):
#         title = self.cleaned_data['title']
        
#         if len(title) < 3:
#             raise forms.ValidationError('Название слишком короткое')
        
#         if title[0].islower():
#             raise forms.ValidationError('Название должно начинаться с заглавной буквы')
        
#         return title  # обязательно вернуть значение

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'is_done': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }