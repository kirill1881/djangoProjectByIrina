from .models import Task
from django.forms import ModelForm, TextInput,Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name","text","time"]
        widgets = {"name":TextInput(attrs={
            "class":"form-control",
            "placeholder":"Введите название"
        }),
            "text": Textarea(attrs={
            "class": "form-control",
            "placeholder": "Введите описание"
        }),
            "time": TextInput(attrs={
            "class": "form-control",
            "placeholder": "Введите время на выполнение"
        }),
        }