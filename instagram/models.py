from django.conf import settings 
from django.db import models
import re

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="instagram/post/%Y/%m/%d")
    caption = models.CharField(max_length=500)
    tag_set = models.ManyToManyField('Tag', blank=True)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.caption

    def extract_tag_list(self):
        return re.findall(r"#([a-zA-Z\dㄱ-힣]+)", self.caption)
    
    # def get_absolute_url(self):
    #     return reverse("", kwargs={"pk": self.pk})
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name