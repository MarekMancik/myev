from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100, blank=True)
    remark = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True)
    content = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    source = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    CATEGORY_CHOICES = [
        ("Home", "Home"),
        ("EV", "Elektroauta"),
        ("Tesla", "Tesla"),
        ("C-EV", "Čínské EV"),
        ("EU-EV", "Evropské EV"),
        ("Other-EV", "Jiné EV"),
        ("Battery", "Baterie"),
        ("Charging", "Nabíjení"),
        ("Technology", "Technologie"),
        ("Ren-Sour", "Obnovitelné zdroje"),
        ("FVE", "Fotovoltaika"),
        ("Wind-E", "Větrná energie"),
        ("Others", "Jiné")
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    # tags = models.ManyToManyField('Tag', related_name='articles')

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
