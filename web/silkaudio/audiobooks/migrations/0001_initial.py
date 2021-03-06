# Generated by Django 2.0.1 on 2018-02-04 04:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Audiobook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('chapters', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.FloatField(default=0)),
                ('recentListen', models.DateTimeField(auto_now=True)),
                ('audiobook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audiobooks.Audiobook')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-recentListen',),
            },
        ),
        migrations.AddField(
            model_name='audiobook',
            name='authors',
            field=models.ManyToManyField(to='audiobooks.Author'),
        ),
        migrations.AlterUniqueTogether(
            name='history',
            unique_together={('user', 'audiobook')},
        ),
    ]
