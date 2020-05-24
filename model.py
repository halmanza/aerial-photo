from wtforms import SubmitField, StringField, validators
from flask_wtf import Form


class RegForm(Form):
    name = StringField('Name', [validators.DataRequired()])
    email = StringField('Email Address', [validators.DataRequired(
    ), validators.Email(), validators.Length(min=6, max=30)])
    inquiry = StringField(
        'Inquiry', [validators.DataRequired(), validators.Length(min=10, max=70)])
    submit = SubmitField('Submit')
