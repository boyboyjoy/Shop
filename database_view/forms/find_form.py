from django.forms import Form, CharField, DateTimeField, DateTimeInput


class FindForm(Form):
    name = CharField()


class FindDateForm(Form):
    date = DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}))
