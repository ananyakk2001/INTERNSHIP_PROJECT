# Generated by Django 5.0.4 on 2024-04-23 06:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariant',
            name='csize',
            field=models.ForeignKey(blank=True, choices=[('s', 's'), ('m', 'm'), ('l', 'l'), ('xl', 'xl')], null=True, on_delete=django.db.models.deletion.CASCADE, to='productapp.sizecategory'),
        ),
    ]
