from django.contrib import admin
from .models import User, HeroSection, AboutSection, BlogPost, TeamMember, Testimonial


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role')
    search_fields = ('username',)


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description')
    search_fields = ('title',)


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'created_at')
    list_filter = ('is_featured', 'category', 'created_at')
    search_fields = ('title', 'category')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
    search_fields = ('name', 'role')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'company_name', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('client_name', 'company_name')

