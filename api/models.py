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
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    short_description = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='hero_images/', blank=True, null=True)
    experience_stat = models.CharField(max_length=50, default='4+ Years')
    projects_stat = models.CharField(max_length=50, default='100+ Projects')
    clients_stat = models.CharField(max_length=50, default='50+ Clients')
    primary_btn_text = models.CharField(max_length=50, default='Get Started')
    primary_btn_url = models.CharField(max_length=255, default='/services/')
    secondary_btn_text = models.CharField(max_length=50, default='Contact Us')
    secondary_btn_url = models.CharField(max_length=255, default='/contact/')
    
    class Meta:
        db_table = 'api_herosection'
        verbose_name = 'Hero Section'
        verbose_name_plural = 'Hero Sections'
        ordering = ['id']
    
    def __str__(self):
        return self.title


class AboutSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)
    video_url = models.CharField(max_length=500, blank=True, null=True)
    journey_subtitle = models.CharField(max_length=100, default='OUR JOURNEY SO FAR')
    journey_title = models.CharField(max_length=255, default='Building the Digital Future with Motion Tech')
    journey_description = models.TextField(blank=True, null=True)
    mission_title = models.CharField(max_length=100, default='Our Mission')
    mission_description = models.TextField(blank=True, null=True)
    vision_title = models.CharField(max_length=100, default='Our Vision')
    vision_description = models.TextField(blank=True, null=True)
    stat_experience = models.CharField(max_length=50, default='4+')
    stat_projects = models.CharField(max_length=50, default='100+')
    stat_clients = models.CharField(max_length=50, default='50+')
    
    class Meta:
        db_table = 'api_aboutsection'
        verbose_name = 'About Section'
        verbose_name_plural = 'About Sections'
        ordering = ['id']
    
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
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'api_teammember'
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'
        ordering = ['order', 'id']
    
    def __str__(self):
        return f"{self.name} - {self.role}"


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    quote = models.TextField()
    logo = models.ImageField(upload_to='testimonial_logos/', blank=True, null=True)
    rating = models.PositiveIntegerField(default=5)
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'api_testimonial'
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ['order', '-id']
    
    def __str__(self):
        return f"{self.client_name} - {self.company_name}"


class Service(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=100, default='bi bi-code-slash', help_text='Bootstrap icon class e.g. bi bi-code-slash')
    icon_color = models.CharField(max_length=50, default='#0d6efd', help_text='HEX or color class e.g. #0d6efd')
    short_description = models.TextField()
    full_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='service_images/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'api_service'
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['order', 'id']

    def __str__(self):
        return self.title


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('hrms', 'HRMS'),
        ('crm', 'CRM'),
        ('pos', 'POS System'),
        ('erp', 'ERP Solution'),
        ('other', 'Other'),
    ]
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    category_tag = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='hrms')
    icon = models.CharField(max_length=100, default='bi bi-people-fill')
    icon_color = models.CharField(max_length=50, default='#2E7D32')
    short_description = models.TextField()
    full_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    demo_url = models.CharField(max_length=500, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'api_product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['order', 'id']

    def __str__(self):
        return self.title


class WhyChooseUs(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.CharField(max_length=100, default='bi bi-laptop')
    icon_color = models.CharField(max_length=50, default='text-primary')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'api_whychooseus'
        verbose_name = 'Why Choose Us'
        verbose_name_plural = 'Why Choose Us'
        ordering = ['order', 'id']

    def __str__(self):
        return self.title


class CoreValue(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100, default='bi bi-lightbulb-fill')
    icon_color = models.CharField(max_length=50, default='#0099FF')
    stat_class = models.CharField(max_length=50, default='base-stat-1', help_text='CSS class: base-stat-1, base-stat-2, base-stat-3')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'api_corevalue'
        verbose_name = 'Core Value'
        verbose_name_plural = 'Core Values'
        ordering = ['order', 'id']

    def __str__(self):
        return self.title


class TechStack(models.Model):
    name = models.CharField(max_length=100)
    technologies = models.CharField(max_length=255)
    icon = models.CharField(max_length=100, default='bi bi-laptop')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'api_techstack'
        verbose_name = 'Technology Stack'
        verbose_name_plural = 'Technology Stacks'
        ordering = ['order', 'id']

    def __str__(self):
        return self.name


class SiteSetting(models.Model):
    company_name = models.CharField(max_length=150, default='Motion Tech Ltd')
    site_title = models.CharField(max_length=255, default='Motion Tech Ltd - Software Development & IT Solutions')
    tagline = models.CharField(max_length=255, default='Crafting Digital Solutions That Businesses Trust')
    logo = models.ImageField(upload_to='site_logos/', blank=True, null=True)
    favicon = models.ImageField(upload_to='site_logos/', blank=True, null=True)
    email = models.CharField(max_length=150, default='info@jatrasoft.com')
    phone = models.CharField(max_length=50, default='+8801601693138')
    address = models.CharField(max_length=255, default='123 Main Street, Dhaka, Bangladesh')
    whatsapp_number = models.CharField(max_length=50, default='8801601693138')
    calendly_url = models.CharField(max_length=500, default='https://calendly.com/hafizul-islam/30min')
    facebook_url = models.CharField(max_length=500, blank=True, null=True, default='https://facebook.com')
    twitter_url = models.CharField(max_length=500, blank=True, null=True, default='https://twitter.com')
    instagram_url = models.CharField(max_length=500, blank=True, null=True, default='https://instagram.com')
    linkedin_url = models.CharField(max_length=500, blank=True, null=True, default='https://linkedin.com')
    github_url = models.CharField(max_length=500, blank=True, null=True)
    footer_about = models.TextField(blank=True, null=True, default='Our mission is to deliver high-quality software solutions that empower businesses and individuals to achieve more with technology.')
    copyright_text = models.CharField(max_length=255, default='Motion Tech Ltd. All rights reserved.')

    class Meta:
        db_table = 'api_sitesetting'
        verbose_name = 'Site Setting'
        verbose_name_plural = 'Site Settings'
        ordering = ['id']

    def __str__(self):
        return self.company_name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        db_table = 'api_contactmessage'
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"

