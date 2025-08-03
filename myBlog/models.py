from django.db import models
from django.urls import reverse
# Create your models here.

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True) 
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('PostModel' , args=[str(self.id)])  # isse us id pr link generate hoga
    