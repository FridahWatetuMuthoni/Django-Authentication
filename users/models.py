from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from PIL import Image

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.CharField(max_length = 250)
    
    def __str__(self):
        return self.username

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(56,56)], format='JPEG', options={'quality':60})
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super(*args, **kwargs).save()
        
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size =(300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)