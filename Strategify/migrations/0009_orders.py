# Generated by Django 4.0.3 on 2022-04-04 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Strategify', '0008_scriplist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('orderid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('scrip', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
                ('transaction_type', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=200)),
                ('username', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='Strategify.userregistration')),
            ],
        ),
    ]
