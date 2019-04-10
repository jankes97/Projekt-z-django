# Generated by Django 2.2 on 2019-04-09 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_extrainfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='id',
        ),
        migrations.AddField(
            model_name='games',
            name='info',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.ExtraInfo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='extrainfo',
            name='rodzaj',
            field=models.IntegerField(choices=[(3, 'FirstPersonShooter'), (4, 'Indie'), (2, 'Horrot'), (0, 'Nieznany'), (1, 'Sci-Fi')], default=0),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, default='', max_length=128)),
                ('stars', models.IntegerField(default=5)),
                ('games', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Games')),
            ],
        ),
    ]