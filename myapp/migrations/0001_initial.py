# Generated by Django 4.2.5 on 2023-09-21 16:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=75)),
                ('year', models.PositiveIntegerField()),
                ('cover_image', models.ImageField(upload_to='cover_images')),
            ],
        ),
        migrations.CreateModel(
            name='Music_genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=75, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25, unique=True)),
                ('full_name', models.CharField(max_length=65)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('profile_pic', models.ImageField(upload_to='profile_pics')),
                ('followers', models.ManyToManyField(blank=True, related_name='usuarios_que_me_siguen', to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=50)),
                ('duration', models.DurationField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='myapp.album')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('content', models.TextField(max_length=750)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.album')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='myapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.music_genre'),
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.user')),
                ('nationality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.nationality')),
            ],
            bases=('myapp.user',),
        ),
        migrations.AddField(
            model_name='album',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.artist'),
        ),
    ]
