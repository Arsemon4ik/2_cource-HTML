from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.title}'


class Artist(models.Model):
    nick = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.nick}'


class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    TYPES = (
        ("POP",'Поп-музыка'),
        ("Rock","Рок-музыка"),
        ("Classic","Классическая-музыка"),
        ("Bluz", 'Блюз'),
        ("Hip-hop","Хип-хоп музыка"),
    )
    genre = models.CharField(choices=TYPES,max_length=7,default="POP")


