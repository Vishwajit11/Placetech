# Generated by Django 4.2.2 on 2023-11-01 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0007_tpocred'),
    ]

    operations = [
        migrations.AddField(
            model_name='stuprnno',
            name='stu_email',
            field=models.EmailField(default='YourDefaultHere', max_length=200),
        ),
    ]