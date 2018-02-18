from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class NotificationForm(FlaskForm):
    notif_title = StringField('title', validators=[DataRequired()])
    notif_desc = StringField('description', validators=[DataRequired()])
    notif_group_id = StringField("group_id",validators=[DataRequired()]) 
    notif_notice_number = StringField('notice_number', validators=[DataRequired()])

    submit = SubmitField('Send Notification')
