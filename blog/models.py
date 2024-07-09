from django.db import models
from user_profile.models import User
from django.utils.text import slugify
from froala_editor.fields import FroalaField 

# Create your models here.

class Category(models.Model):
    category=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(null=True,blank=True)
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.category
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.category)
        super().save(*args, **kwargs)


    
class Tag(models.Model):
    tags=models.CharField(max_length=150)
    slug=models.SlugField(null=True,blank=True)
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.tags
    
    def save(self,*args, **kwargs):

        self.slug=slugify(self.tags)
        super().save(*args, **kwargs)






class Blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_blog')
    category=models.ForeignKey(Category,related_name='category_blogs',on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tag,related_name='blog_tag',blank=True)
    likes=models.ManyToManyField(User,related_name='user_like')
    title=models.CharField(max_length=250)
    slug=models.SlugField(null=True,blank=True)
    description=FroalaField ()
    banner=models.ImageField(upload_to='blog_banner')
    create_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):

        self.slug=slugify(self.title)
        super().save(*args, **kwargs)

    


class Comment(models.Model):
    user=models.ForeignKey(User,related_name='user_comment',on_delete=models.CASCADE)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blog_comment')
    text=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.text

class Reply(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_reply')  
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE,related_name='comment_reply')  




class Contact(models.Model):
    phone_number=models.CharField(max_length=15)
    email=models.EmailField()
    address=models.CharField(max_length=150)

    def __str__(self):
        return self.email