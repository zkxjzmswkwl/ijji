# Generated by Django 5.0 on 2024-03-01 21:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="GameDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "map",
                    models.CharField(
                        choices=[
                            ("Antarctic Peninsula", "Antarctic Peninsula"),
                            ("Ilios", "Ilios"),
                            ("Nepal", "Nepal"),
                            ("Samoa", "Samoa"),
                            ("Lijiang Tower", "Lijiang Tower"),
                            ("Oasis", "Oasis"),
                            ("Circuit Royal", "Circuit Royal"),
                            ("Havana", "Havana"),
                            ("Rialto", "Rialto"),
                            ("Route 66", "Route 66"),
                            ("Dorado", "Dorado"),
                            ("Junkertown", "Junkertown"),
                            ("Watchpoint: Gibraltar", "Watchpoint: Gibraltar"),
                            ("Shambali Monastery", "Shambali Monastery"),
                            ("New Junk City", "New Junk City"),
                            ("Suravasa", "Suravasa"),
                            ("Blizzard World", "Blizzard World"),
                            ("Eichenwalde", "Eichenwalde"),
                            ("Hollywood", "Hollywood"),
                            ("King's Row", "King's Row"),
                            ("Midtown", "Midtown"),
                            ("Paraiso", "Paraiso"),
                            ("Colosseo", "Colosseo"),
                            ("Esperanca", "Esperanca"),
                            ("New Queen Street", "New Queen Street"),
                        ],
                        max_length=200,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Vod",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("video", models.FileField(upload_to="videos/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("played_by", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "tags",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("owcs", "Overwatch Championship Series"),
                            ("owl", "Overwatch League"),
                            ("owcn", "Overwatch Contenders"),
                            ("NA", "North America"),
                            ("EU", "Europe"),
                            ("EMEA", "Europe, Middle East, and Africa"),
                            ("TANK", "Tank"),
                            ("DPS", "Damage"),
                            ("SUP", "SUPPORT"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "belongs_to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]