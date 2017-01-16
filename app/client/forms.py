from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,	DateTimeField, IntegerField, TextField
from wtforms import ValidationError
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms.fields.html5 import DateField
from wtforms.widgets.core import HTMLString, html_params, escape

class DateTimeWidget(object):
	def __call__(self, field, **kwargs):
		kwargs.setdefault('type', 'input')
		# Allow passing title= or alternately use field.description
		title = kwargs.pop('title', field.description or '')
		field_id = kwargs.pop('id', field.id)
		params = html_params(title=title, **kwargs)

					
		html  =	  "<div style='overflow:hidden;'> " \
				+ "    <div class='form-group'> " \
				+ "        <div class='row'> " \
				+ "            <div class='col-md-12'> " \
				+ "                <div id='%s'></div> " \
				+ "            </div> " \
				+ "        </div> " \
				+ "    </div> " \
				+ "</div> " 

			
		
		return HTMLString(html % (field_id))

class BookingForm(FlaskForm):
	time = DateTimeField('time', format='%Y-%m-%d %H:%M', widget=DateTimeWidget())
	#time = DateTimeField('Date', format='%Y-%m-%d %H:%M', widget=DateTimePickerWidget())
	hours = IntegerField()
	start = IntegerField()
	submit = SubmitField()
	
class CommentForm(FlaskForm):
	score = IntegerField('Score', validators=[Required()])
	text = TextField('Commentaire', validators=[Required(), Length(1,300)])
	submit = SubmitField()