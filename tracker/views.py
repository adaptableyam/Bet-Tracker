from django.shortcuts import render
from .forms import BetForm

# Create your views here.
def index(request):
    return render(request, 'tracker/index.html')

def add_bet(request):
    bet_form = BetForm()
    return render(request, 'tracker/add-bet.html', {'bet_form':bet_form})