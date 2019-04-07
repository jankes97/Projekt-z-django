# Generated by Django 2.1.7 on 2019-04-04 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190404_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, default='', max_length=250)),
                ('stars', models.IntegerField(default=5)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Game')),
            ],
        ),
        migrations.AlterField(
            model_name='extrainfo',
            name='STATUS',
            field=models.IntegerField(choices=[(0, 'NIEZNANY'), (4, 'USZKODZONY'), (3, 'UKONCZONY'), (2, 'OCZEKUJACY'), (1, 'ROZPOCZETY')], default=0),
        ),
    ]
