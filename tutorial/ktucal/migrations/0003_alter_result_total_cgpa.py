# Generated by Django 4.1.7 on 2023-03-21 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ktucal', '0002_rename_name_result_name_rename_rollno_result_rollno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='Total_CGPA',
            field=models.FloatField(default=0),
        ),
    ]