from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import Length


class CommentForm(FlaskForm):
    class Meta:
        csrf = False

    comment = TextAreaField(validators=[Length(min=1)])

    submit = SubmitField('Add Comment')
