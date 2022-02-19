from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html

# Create your models here.
class Temperature(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    temperature = models.IntegerField()

    class Meta:
        ordering = ['-created_on']


class CO2Level(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    co2_level = models.IntegerField()

    class Meta:
        ordering = ['-created_on']


class Humidity(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    humidity = models.IntegerField()

    class Meta:
        ordering = ['-created_on']


# Image Model
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class PiCameraImage(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    upload = models.ImageField(upload_to=user_directory_path)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # If you want to show the media files in the list display in the admin panel:
    def image_tag(self):
        return format_html('<img href="{0}" src="{0}" width="150" height="150" />'.format(self.upload.url))

    image_tag.allow_tags = True
    image_tag.short_description = 'Image'

    class Meta:
        ordering = ['-created_on']
