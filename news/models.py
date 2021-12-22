from django.db import models
from users.models import Author 
# Create your models here.

class Article(models.Model):
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    class Meta:
        #db_table = 'article_article'
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"


    def __str__(self):
        return self.headline