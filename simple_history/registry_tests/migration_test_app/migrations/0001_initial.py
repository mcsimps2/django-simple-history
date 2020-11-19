# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-18 21:58
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="DoYouKnow",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                )
            ],
        ),
        migrations.CreateModel(
            name="HistoricalYar",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical yar",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
        ),
        migrations.CreateModel(
            name="Yar",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                )
            ],
        ),
        migrations.CreateModel(
            name="WhatIMean",
            fields=[
                (
                    "doyouknow_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="migration_test_app.DoYouKnow",
                    ),
                )
            ],
            bases=("migration_test_app.doyouknow",),
        ),
        migrations.AddField(
            model_name="yar",
            name="what",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="migration_test_app.WhatIMean",
            ),
        ),
        migrations.AddField(
            model_name="historicalyar",
            name="what",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="migration_test_app.WhatIMean",
            ),
        ),
    ]
