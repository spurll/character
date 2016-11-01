from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, HiddenField
from wtforms.fields.html5 import IntegerField
from wtforms.validators import Required, NumberRange


class TemplateForm(Form):
    hidden = HiddenField("Hidden", validators=[Required()])
    integer = IntegerField("Int", default=0, validators=[NumberRange(min=0)])
