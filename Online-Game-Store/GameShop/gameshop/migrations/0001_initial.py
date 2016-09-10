# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, unique=True)),
                ('description', models.CharField(max_length=300)),
                ('release_date', models.DateField(auto_now_add=True)),
                ('publisher', models.CharField(blank=True, max_length=225)),
                ('genre', models.CharField(choices=[('SH', 'Shooter'), ('AA', 'Action-adventure'), ('RPG', 'Role-playing game'), ('SP', 'Sports'), ('RTS', 'Real-time strategy'), ('HR', 'Horror'), ('MMO', 'Massive multiplayer online')], max_length=225)),
                ('source', models.URLField(max_length=225, unique=True)),
                ('price', models.FloatField()),
                ('game_developer', models.ForeignKey(related_name='DeveloperGames', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('library', models.ManyToManyField(to='gameshop.Game')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GameSale',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('timeBought', models.DateTimeField(auto_now_add=True)),
                ('gamePrice', models.FloatField()),
                ('game', models.ForeignKey(to='gameshop.Game')),
            ],
        ),
        migrations.CreateModel(
            name='GameSave',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('gameState', models.CharField(max_length=2250)),
                ('saveTime', models.DateTimeField(auto_now_add=True)),
                ('game', models.ForeignKey(to='gameshop.Game')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-saveTime'],
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('points', models.PositiveIntegerField()),
                ('game', models.ForeignKey(related_name='GameScores', to='gameshop.Game')),
                ('user', models.ForeignKey(related_name='UserScores', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-points'],
            },
        ),
    ]
