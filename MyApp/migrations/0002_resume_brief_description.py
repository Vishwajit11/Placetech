# Generated by Django 4.2.2 on 2023-10-22 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='brief_description',
            field=models.TextField(default='YourDefaultHere', max_length=1000),
        ),
    ]
