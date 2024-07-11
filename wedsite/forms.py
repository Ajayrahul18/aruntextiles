
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, PasswordField, EmailField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, length, NumberRange, Email
from flask_wtf.file import FileField, FileRequired


class UserProfileUpdateForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = IntegerField('Phone', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Update')


class UserSigupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    user_name = StringField('User Name', validators=[DataRequired()])
    password_1 = PasswordField('Enter Your Password', validators=[DataRequired(), length(min=6)])
    password_2 = PasswordField('Confirm Your Password', validators=[DataRequired(), length(min=6)])
    submit = SubmitField('Submit & Register')
    
class AdminLoginForm(FlaskForm):
    username = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Enter Your Password', validators=[DataRequired(), length(min=6)])
    submit = SubmitField('Sign Up')

class UserLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Enter Your Password', validators=[DataRequired(), length(min=6)])
    submit = SubmitField('Sign Up')


class ShopItemsForm(FlaskForm):
    choices = [('all', 'All Products'),('newBorn', 'New Born'), ('kids', 'Kids'), ('boys', 'Boys'), ('girls', 'Girls'), ('men', 'Men'), ('women', 'Woman')]
    product_name = StringField('Name of Product', validators=[DataRequired()])
    current_price = FloatField('Current Price', validators=[DataRequired()])
    previous_price = FloatField('Previous Price', validators=[DataRequired()])
    product_picture = FileField('Product Picture', validators=[DataRequired()])
    product_picture_zoom = FileField('Zoom Picture', validators=[DataRequired()])
    product_tag = SelectField('Product Filter', choices=choices, default='all')

    add_product = SubmitField('Add Product')
    update_product = SubmitField('Update')

class InstaForm(FlaskForm):
    product_picture = FileField('Product Picture', validators=[DataRequired()])
    
    add_product = SubmitField('Add Product')



