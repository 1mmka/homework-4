from django.db import models
from django.core import validators
from easy_thumbnails.fields import ThumbnailerImageField

# Create your models here.
class Image(models.Model):
    img = ThumbnailerImageField(upload_to='images',validators=[validators.FileExtensionValidator(
        allowed_extensions=('png','jpg','jpeg','gif','ico')
    )])
    full_image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.img.url