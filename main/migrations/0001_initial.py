# Generated by Django 4.2.5 on 2023-10-17 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('mail', models.EmailField(default='', max_length=50)),
                ('message', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
