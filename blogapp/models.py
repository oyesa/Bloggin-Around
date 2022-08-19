from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User



# Create your models here.
class Blogpost(models.Model):
  title = models.CharField(max_length= 255, default=True)
  description = models.TextField('Description', blank=True)
  image = CloudinaryField('image', blank=True, null=True)
  likes_count = models.IntegerField(default=0)
  comment_count = models.IntegerField(default=0)
  date_posted = models.DateField(auto_now=True)

  #functions
  def save_blogpost(self):
    self.save()

  def update_blogpost(self):
    self.update_blogpost()

  def delete_blogpost(self):
    self.delete()


class Comments(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  comment = models.CharField(max_length= 500)


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
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.likes

