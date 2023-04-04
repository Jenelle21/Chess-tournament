# Generated by Django 4.1.7 on 2023-04-01 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('white_player', models.CharField(max_length=255)),
                ('black_player', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('result', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('move_number', models.IntegerField()),
                ('color', models.CharField(max_length=5)),
                ('move_san', models.CharField(max_length=10)),
                ('analysis', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chess_engine.game')),
            ],
        ),
    ]
