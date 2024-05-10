
from django.forms import ModelForm, Select, NumberInput, DateInput, RadioSelect
from .models import Bet


class BetForm(ModelForm):
    class Meta:

        tailwind_class = "border rounded-lg shadow-sm border-gray-300 focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 px-5 py-3"
        tailwind_class_select = "border rounded-lg shadow-sm border-gray-300 focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 px-7 py-3"
        tailwind_class_radio = "focus:ring-offset-0 focus:ring-white focus:outline-none text-indigo-500"
        model = Bet
        fields = (
            'game',
            'amount',
            'decimal_odds',
            'win',
            'profit',
            'bet_date',
        )
        widgets = {
            'game': Select(choices=Bet.Game.choices, attrs={'onchange': "toggleOdds(this.value);", 'class': tailwind_class_select,}),
            'amount': NumberInput(attrs={'class': tailwind_class}),
            'decimal_odds': NumberInput(attrs={'class': tailwind_class, 'id': "odds_input"}),
            'win': RadioSelect(choices=Bet.BOOL_CHOICES, attrs={'class': tailwind_class_radio, 'onchange': "toggleProfit(this.value);",}),
            'profit': NumberInput(attrs={'class': tailwind_class, 'id': "profit_input"}),
            'bet_date': DateInput(format='%d/%m/%Y', attrs={'class': tailwind_class}),
        }
