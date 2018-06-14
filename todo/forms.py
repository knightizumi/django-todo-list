from django.forms import ModelForm, Form, BooleanField

from .models import Todo

class TodoModelForm(ModelForm):
    class Meta:
        model = Todo
        exclude=['creator']
    def save(self, user, commit=True):
        todo = super().save(commit=False)  # save without write database
        todo.creator = user
        todo.save()  # write in db

        self.save_m2m()   # self==>this
        return todo

class DeleteConfirmForm(Form):
    # 繼承form
    check=BooleanField(label='你確定要刪除嗎?')
