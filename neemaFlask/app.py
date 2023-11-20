from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'


class SponsorForm(FlaskForm):
    choices = [('money', 'Donated Money'), ('resources', 'Donated Resources')]
    sponsor_name = StringField('Sponsor Name', validators=[DataRequired()])
    donation_type = SelectField('Donation Type',
                                choices=choices,
                                validators=[DataRequired()])
    donation_details = TextAreaField('Donation Details', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def add_sponsor():
    form = SponsorForm()

    if form.validate_on_submit():
        # Process the form data (e.g., save to a database)
        sponsor_name = form.sponsor_name.data
        donation_type = form.donation_type.data
        donation_details = form.donation_details.data

        # Here you can handle the data as needed (e.g., save to a database)

        return f'Sponsor added: {sponsor_name}, Donation Type: {donation_type}, Details: {donation_details}'

    return render_template('add_sponsor.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
