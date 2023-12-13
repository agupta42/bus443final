# Generated by Django 4.0.4 on 2022-05-03 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentid', models.IntegerField()),
                ('firstname', models.CharField(max_length=500)),
                ('lastname', models.CharField(max_length=500)),
                ('major', models.CharField(max_length=150)),
                ('year', models.CharField(max_length=500)),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]
