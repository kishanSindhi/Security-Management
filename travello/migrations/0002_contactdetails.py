# Generated by Django 4.0.3 on 2022-04-09 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=11)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]