from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Nationality(models.Model):
    country = models.CharField(max_length=75, unique=True)

class Music_genre(models.Model):
    genre_name= models.CharField(max_length=50, unique= True)


class User(models.Model):
    username = models.CharField(max_length=25, unique=True)
    full_name = models.CharField(max_length=65)
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(upload_to= 'profile_pics')
    followers = models.ManyToManyField('self', symmetrical='False', related_name= 'usuarios_que_me_siguen', blank=True)


class Artist(User):
    nationality = models.ForeignKey(Nationality, on_delete= models.CASCADE)


class Album(models.Model):
    album_name = models.CharField(max_length=75)
    year = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to='cover_images')
    author = models.ForeignKey(Artist, on_delete= models.CASCADE)
    genre= models.ForeignKey(Music_genre, on_delete= models.CASCADE)
    


class Song(models.Model):
    song_name= models.CharField(max_length=50)
    duration = models.DurationField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    qualification = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    content = models.TextField(max_length=750)
    creation_date = models.DateField(auto_now_add=True)




