# Generated by Django 2.1.7 on 2019-04-04 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20190404_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraOpi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat', models.IntegerField(choices=[(0, 'Nieznany'), (2, 'Aktywny'), (3, 'Ukonczony'), (4, 'Uszkodzony'), (1, 'Oczekujacy')], default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='game',
            name='info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.ExtraOpi'),
        ),
        migrations.DeleteModel(
            name='ExtraOpis',
        ),
    ]
