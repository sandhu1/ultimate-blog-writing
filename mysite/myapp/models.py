from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    entry_title=models.CharField(max_length=50)
    entry_text=models.TextField()
    entry_date=models.DateTimeField(auto_now_add=True)
    entry_author=models.ForeignKey(User,on_delete=models.CASCADE)


#plural name of entry object
    class Meta:
        verbose_name_plural='entries'

#name of the object changes to entry title
    def __str__(self):
        return self.entry_title




# Create your models here.
