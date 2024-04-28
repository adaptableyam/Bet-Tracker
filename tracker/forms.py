
from django.forms import ModelForm
from .models import Bet

class BetForm(ModelForm):
    class Meta:

        model = Bet
        fields = (
            'game',
            'amount',
            'decimal_odds',
            'win',
            'bet_date',
        )