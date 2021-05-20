# Generated by Django 3.2.3 on 2021-05-18 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='district_mapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_id', models.IntegerField()),
                ('district_id', models.IntegerField()),
                ('district_name', models.CharField(max_length=100)),
                ('state_name', models.CharField(max_length=100)),
            ],
        ),
    ]
