# Generated by Django 2.1.7 on 2019-04-06 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20190405_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rodzaj', models.IntegerField(choices=[(1, 'Survival-Horror'), (3, 'Survival'), (0, 'Sci-Fi'), (4, 'Race'), (2, 'Horror')], default=0)),
            ],
        ),
    ]