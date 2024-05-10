from django.db import models
from django.utils import timezone

# Create your models here.
"""
The bet class needs:
- type: Sports, roulette, etc
- amount: float e.g £19.50
- odds: e.g 3/1 (to convert odds to decimal its numerator/denominator + 1) so 3/1 would be 4 in decimal
- win: true/false (false by default) 
    if false, loss column is just amount. 
    if true, profit is (decimal odds * amount - original bet amount)
- profit: if no win, = 0. otherwise use formula above
- loss: if win = 0. otherwise, = amount
"""

class Bet(models.Model): 
    class Game(models.TextChoices):
        ROULETTE = "RLT", "Roulette"
        BLACKJACK = "BKJ", "Blackjack"
        BACCARAT = "BAC", "Baccarat"
        SLOTS = "SLT", "Slots"
        CRAPS = "CPS", "Craps"
        POKER = "PKR", "Poker"
        SPORTS = "SPT", "Sports"
        OTHER = "OTH", "Other"
   
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    # Offer a predetermined selection of most popular games, to make showing data easier.
    game = models.CharField(max_length=100, choices=Game.choices, default=Game.ROULETTE)
    # Amount wagered up to 10,000,000.00
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # keeping odds to decimal in order to speed up development, although less commonly used than ratio odds
    decimal_odds = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2)
    # Simple Win or Loss box, defaults to loss
    win = models.BooleanField(choices=BOOL_CHOICES, default=False)
    # Profit column, will be negative value of 'amount' if 'win' == false
    # if 'win' == True: profit = amount * odds  
    profit = models.DecimalField(max_digits=12, decimal_places=2)
    # Imported datetime module to get an overridable default value of current user date.
    bet_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.game} (£{self.amount}) {self.bet_date}"

