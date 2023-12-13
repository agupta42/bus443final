# Generated by Django 4.0.4 on 2022-05-04 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_detailsbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookid', models.IntegerField()),
                ('booktitle', models.CharField(max_length=2000)),
                ('authorname', models.CharField(max_length=2000)),
                ('currentlycheckedout', models.CharField(max_length=10)),
                ('numberoftimescheckedout', models.IntegerField()),
            ],
        ),
    ]
