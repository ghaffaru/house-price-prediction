from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired


class PredictionForm(FlaskForm):
    bedrooms = IntegerField('Bedrooms', validators=[DataRequired()])
    bathrooms = IntegerField('Bathrooms', validators=[DataRequired()])
    sqft_living = IntegerField('Sqtf living', validators=[DataRequired()])
    sqft_lot = IntegerField('Sqft lot', validators=[DataRequired()])
    floors = IntegerField('Floors', validators=[DataRequired()])
    sqft_above = IntegerField('Sqft above', validators=[DataRequired()])
    sqft_lot15 = IntegerField('Sqft lot15', validators=[DataRequired()])
    yr_built = IntegerField('Yr built', validators=[DataRequired()])
    condition = IntegerField('Condition', validators=[DataRequired()])
    zipcode = IntegerField('Zip code', validators=[DataRequired()])
    submit = SubmitField('Predict')