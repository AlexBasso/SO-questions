# Generated by Django 4.1.3 on 2022-11-22 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_school_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='studentGrade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
