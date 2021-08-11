from django.db import models

# Create your models here.
class MakeTeam(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    content = models.TextField()
    num = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:80]