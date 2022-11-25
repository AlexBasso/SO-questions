# Generated by Django 4.1.3 on 2022-11-20 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolName', models.CharField(max_length=200, unique=True)),
                ('className', models.CharField(max_length=200, unique=True)),
                ('studentName', models.CharField(max_length=200, unique=True)),
                ('studentGrade', models.IntegerField()),
                ('professorName', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'unique_together': {('schoolName', 'className'), ('className', 'professorName'), ('className', 'studentName')},
            },
        ),
    ]
