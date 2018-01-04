from django.db import models

# Create your models here.
from datetime import date
from django.urls import reverse #Used to generate urls by reversing the URL patterns
from django.contrib.auth.models import User #Blog author or commenter



"""class MyModelName(models.Model):
    
    A typical class defining a model, derived from the Model class.
    

    # Fields
    my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")
    ...

    # Metadata
    class Meta: 
        ordering = ["-my_field_name"]

    # Methods
    def get_absolute_url(self):
         
         Returns the url to access a particular instance of MyModelName.
         
         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        
        String for representing the MyModelName object (in Admin site etc.)
        
        return self.field_name"""

class BlogAuthor(models.Model):
    """
    Model representing a blogger.
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=400, help_text="Enter your bio details here.")

    def get_absolute_url(self):
        """
        Returns the url to access a particular blog-author instance.
        """
        #return reverse('blogs-by-author', args=[str(self.id)])
        return reverse('blogauthor-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.user.username

class Collection(models.Model):
    """
    Model representing a blogger.
    """
    collection = models.CharField(max_length=200)

    def get_absolute_url(self):
        """
        Returns the url to access a particular blog-author instance.
        """
        #return reverse('blogs-by-author', args=[str(self.id)])
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.collection

class Blog(models.Model):
    """
    Model representing a blog post.
    """
    name = models.CharField(max_length=200)
    #author = models.CharField(max_length=200,default="nothing")
    author = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True)
  	#Foreign Key used because Blog can only have one author/User, but bloggsers can have multiple blog posts.
    description = models.TextField(max_length=2000, help_text="Write your blog post here.")
    post_date = models.DateField(default=date.today)
    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ["-post_date"]
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular blog instance.
        """
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name

class Movie(models.Model):
    #title = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=400,help_text="Enter name of movie")
    director = models.CharField(max_length=400,help_text="Enter name of director")
    blurb = models.TextField(max_length=2000,help_text="Enter movie blurb",null=True,blank=True)
    collection = models.CharField(max_length=400,help_text="Enter name of collection")
    artwork = models.ImageField()
    artwork_url = models.CharField(max_length=400,help_text="Enter url of movie artwork",null=True,blank=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particlar movie instance
        """
        return reverse('movie-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name #hehe
