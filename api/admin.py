from django.contrib import admin
from .models import (
    User, HeroSection, AboutSection, BlogPost, TeamMember, Testimonial,
    Service, Product, WhyChooseUs, CoreValue, TechStack, SiteSetting, ContactMessage
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role')
    search_fields = ('username',)


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'experience_stat', 'projects_stat', 'clients_stat')
    search_fields = ('title', 'subtitle', 'short_description')


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'mission_title', 'vision_title')
    search_fields = ('title', 'description', 'mission_description', 'vision_description')


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'created_at')
    list_filter = ('is_featured', 'category', 'created_at')
    search_fields = ('title', 'category')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order', 'is_featured')
    list_editable = ('order', 'is_featured')
    list_filter = ('is_featured',)
    search_fields = ('name', 'role')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'company_name', 'rating', 'order', 'is_published')
    list_editable = ('order', 'is_published')
    list_filter = ('is_published', 'rating')
    search_fields = ('client_name', 'company_name', 'quote')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category_tag', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active', 'category_tag')
    search_fields = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')


@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ('title', 'stat_class', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')


@admin.register(TechStack)
class TechStackAdmin(admin.ModelAdmin):
    list_display = ('name', 'technologies', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'technologies')


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'phone', 'address')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_editable = ('is_read',)
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)

