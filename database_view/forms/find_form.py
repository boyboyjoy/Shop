from django.forms import Form, CharField


class FindForm(Form):
    name = CharField()
