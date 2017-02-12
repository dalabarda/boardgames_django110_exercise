from django.forms import ModelForm
from .models import Invitation, Move, BOARD_SIZE
from django.core.exceptions import ValidationError
from django import forms

class InvitationForm(forms.ModelForm):
	class Meta:
		model = Invitation
		exclude = ['from_user']
		fields = '__all__' # Or a list of the fields that you want to include in your form


class MoveForm(ModelForm):
	class Meta:
		model = Move
		exclude = ('game', 'by_first_player', 'comment')

		def clean(self):
			game = self.instance.game
			x = self.cleaned_data.get("x")
			y = self.cleaned_data.get("y")
			if not game or \
				not game.status == "A" or \
				not game.is_empty(x, y):
					raise ValidationError("Illegal move")
			return self.cleaned_data
