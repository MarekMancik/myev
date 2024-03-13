from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    remark = RichTextField(null=True, blank=True)



class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', name=None, width_field=500, height_field=400)
    source = models.CharField(max_length=100)
    created_at =models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    CATEGORY_CHOICES = [
        ("Home", "Home"),
        ("EV", "Eletroauta"),
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
    tags = models.ManyToManyField('Tag', related_name='articles')





class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

