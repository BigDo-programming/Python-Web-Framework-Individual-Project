# Generated by Django 4.1.3 on 2022-11-16 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_app', '0004_baseingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baserecipe',
            name='ingredient',
            field=models.ManyToManyField(blank=True, to='recipes_app.baseingredient'),
        ),
    ]