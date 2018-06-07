from django.forms import ModelForm, Form, BooleanField

from .models import Todo

class TodoModelForm(ModelForm):
    class Meta:
        model = Todo
        exclude=['creator']



class DeleteConfirmForm(Form):
    # 繼承form
    check=BooleanField(label='你確定要刪除嗎?')
