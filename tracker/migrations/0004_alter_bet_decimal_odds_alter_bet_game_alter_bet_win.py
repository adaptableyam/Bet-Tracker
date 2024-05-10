# Generated by Django 5.0.4 on 2024-05-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tracker", "0003_alter_bet_bet_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bet",
            name="decimal_odds",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=8, null=True
            ),
        ),
        migrations.AlterField(
            model_name="bet",
            name="game",
            field=models.CharField(
                choices=[
                    ("RLT", "Roulette"),
                    ("BKJ", "Blackjack"),
                    ("BAC", "Baccarat"),
                    ("SLT", "Slots"),
                    ("CPS", "Craps"),
                    ("PKR", "Poker"),
                    ("SPT", "Sports"),
                    ("OTH", "Other"),
                ],
                default="RLT",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="bet",
            name="win",
            field=models.BooleanField(
                choices=[(True, "Yes"), (False, "No")], default=False
            ),
        ),
    ]
