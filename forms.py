from flask_wtf import Form, BooleanField, TextField, PasswordField, validators, RecaptchaField, TextAreaField

class RegistrationForm(Form):
    password = PasswordField('Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.Length(min=8, max=32)
    ])
    confirm = PasswordField('Confirm Password')
    fname = TextField('First Name', [validators.Length(min=2, max=32), validators.Required()])
    lname = TextField('Last Name', [validators.Length(min=2, max=32), validators.Required()])
    email1 = TextField('Email', [validators.Length(min=5, max=48),validators.Required(),
                                 validators.Email(message='Either email is invalid or already registered.')])
    recaptcha = RecaptchaField(validators.Required())
    
class LoginForm(Form):
    email = TextField('Email', [validators.Length(min=4, max=64),validators.Required(),
                                validators.Email()])
    password = PasswordField('Password', [
        validators.Required(),
        validators.Length(min=8, max=32)
    ])

class OpenIDForm(Form):
    openid = TextField('OpenID', [validators.Length(min=2, max=64), validators.Optional()])
    googleid = TextField('GoogleID', [validators.Length(min=2, max=64), validators.Optional()])
    yahooid = TextField('YahooID', [validators.Length(min=2, max=64), validators.Optional()])

class QuestionForm(Form):
    question = TextField('Question', [validators.Length(min=4, max=200), validators.Required()])
    description = TextAreaField('', [validators.Length(min=20, max=5000), validators.Required()])
    tags = TextField('Tags', [validators.Length(min=1, max=100), validators.Required()])

class AnswerForm(Form):
    answer = TextAreaField('', [validators.Length(min=20, max=5000), validators.Required()])

class CommentForm(Form):
    comment = TextAreaField('', [validators.Length(min=20, max=5000), validators.Required()])

class ProfileForm(Form):
    fname = TextField('First Name', [validators.Length(min=2, max=32), validators.Required()])
    lname = TextField('Last Name', [validators.Length(min=2, max=32), validators.Required()])
    email1 = TextField('Email', [validators.Length(min=5, max=48),validators.Required(),
                                 validators.Email(message='Either email is invalid or already registered.')])
    recaptcha = RecaptchaField(validators.Required())

class TagForm(Form):
    info = TextAreaField('', [validators.Length(min=20, max=5000), validators.Required()])

class PasswordResetForm(Form):
    password = PasswordField('Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.Length(min=8, max=32)
    ])
    confirm = PasswordField('Confirm Password')

class EmailForm(Form):
    email = TextField('Email', [validators.Length(min=5, max=48),validators.Required(),
                                 validators.Email(message='Email is invalid')])
