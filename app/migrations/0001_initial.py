# Generated by Django 4.2.3 on 2023-07-19 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=140)),
            ],
        ),
    ]
