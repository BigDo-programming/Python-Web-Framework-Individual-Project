# Generated by Django 4.1.3 on 2022-11-16 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_app', '0003_alter_ingredient_options_remove_ingredient_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_number', models.FloatField(blank=True, null=True)),
                ('quantity', models.CharField(blank=True, max_length=50, null=True)),
                ('order_index', models.PositiveIntegerField(blank=True, null=True)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recipes_app.food')),
                ('preparation_method', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='recipes_app.preparationmethod')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='recipes_app.unit')),
            ],
        ),
    ]