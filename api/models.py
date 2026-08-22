from django.db import models
from django.core.files.storage import default_storage
import bcrypt


class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password_hash = models.CharField(max_length=255)
    role = models.CharField(max_length=50, default='Admin')
    
    class Meta:
        db_table = 'api_user'
    
    def set_password(self, raw_password):
        self.password_hash = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, raw_password):
        try:
            return bcrypt.checkpw(raw_password.encode('utf-8'), self.password_hash.encode('utf-8'))
        except:
            return False
    
    def __str__(self):
        return self.username


class HeroSection(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='hero_images/', blank=True, null=True)
    
    class Meta:
        db_table = 'api_herosection'
        verbose_name = 'Hero Section'
        verbose_name_plural = 'Hero Sections'
    
    def __str__(self):
        return self.title


class AboutSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)
    video_url = models.CharField(max_length=500, blank=True, null=True)
    
    class Meta:
        db_table = 'api_aboutsection'
        verbose_name = 'About Section'
        verbose_name_plural = 'About Sections'
    
    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    short_description = models.TextField()
    long_description = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    video_url = models.CharField(max_length=500, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    tags = models.CharField(max_length=500, blank=True, null=True)  # comma-separated
    author_name = models.CharField(max_length=100, blank=True, null=True)
    author_image = models.ImageField(upload_to='author_images/', blank=True, null=True)
    read_time_minutes = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    class Meta:
        db_table = 'api_blogpost'
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='team_photos/', blank=True, null=True)
    facebook_url = models.CharField(max_length=500, blank=True, null=True)
    instagram_url = models.CharField(max_length=500, blank=True, null=True)
    linkedin_url = models.CharField(max_length=500, blank=True, null=True)
    github_url = models.CharField(max_length=500, blank=True, null=True)
    
    class Meta:
        db_table = 'api_teammember'
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'
    
    def __str__(self):
        return f"{self.name} - {self.role}"


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    quote = models.TextField()
    logo = models.ImageField(upload_to='testimonial_logos/', blank=True, null=True)
    is_published = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'api_testimonial'
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ['-id']
    
    def __str__(self):
        return f"{self.client_name} - {self.company_name}"

