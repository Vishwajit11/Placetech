# Generated by Django 4.2.2 on 2023-11-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0012_resume_famskills_resume_famtech_resume_protech_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='project_tech',
            field=models.CharField(default='YourDefaultHere', max_length=100),
        ),
    ]
