# Generated by Django 4.0.2 on 2022-04-20 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_remove_survey_id_survey_survey_id_alter_survey_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='date',
            field=models.DateField(null=True),
        ),
    ]