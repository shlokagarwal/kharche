# Generated by Django 2.2.7 on 2019-11-21 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('monthly_max_limit', models.IntegerField()),
                ('daily_max_limit', models.IntegerField()),
                ('join_date', models.DateTimeField(verbose_name='Joining Date')),
                ('preferred_cateogies', models.CharField(default="['Food & Beeverages', 'Clothes', 'Fuel', 'Shopping', 'Entertainment', 'Health', 'Holiday']", max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('expense_date', models.DateTimeField(verbose_name='expense date')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=19)),
                ('additional_note', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenses.User')),
            ],
        ),
    ]
