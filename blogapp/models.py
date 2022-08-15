from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User



# Create your models here.
class Blogpost(models.Model):
  name = models.CharField(max_length= 10000)
  description = models.CharField(max_length= 100000)
  image = CloudinaryField('image', blank=True, null=True)

  #functions
  def save_blogpost(self):
    self.save()

  def update_blogpost(self):
    self.update_blogpost()

  def delete_blogpost(self):
    self.delete()


class Comments(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  comment = models.CharField(max_length= 1000)


  #functions
  def save_comment(self):
    self.save()

  def update_comment(self):
    self.update_comment()

  def delete_comment(self):
    self.delete()

  def __str__(self):
    return self.comment



class Likes(models.Model):
  blogpost = models.ForeignKey(Blogpost, on_delete=models.CASCADE)

  def __str__(self):
    return self.likes

