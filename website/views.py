from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import models
from api.models import HeroSection, AboutSection, BlogPost, TeamMember
from .forms import ContactForm


def home(request):
    heroes = HeroSection.objects.all()[:1]
    about = AboutSection.objects.first()
    blogs = BlogPost.objects.all().order_by('-created_at')[:6]  # Latest 6 blogs for home page
    team_members = TeamMember.objects.all()[:4]  # First 4 team members for home page
    
    context = {
        'heroes': heroes,
        'about': about,
        'blogs': blogs,
        'team_members': team_members,
    }
    return render(request, 'website/home.html', context)


def about(request):
    about = AboutSection.objects.first()
    context = {'about': about}
    return render(request, 'website/about.html', context)


def blog(request):
    blogs = BlogPost.objects.all().order_by('-created_at')
    
    # Get search query
    search_query = request.GET.get('search', '').strip()
    category = request.GET.get('category', '').strip()
    
    # Filter by search
    if search_query:
        blogs = blogs.filter(
            models.Q(title__icontains=search_query) |
            models.Q(short_description__icontains=search_query) |
            models.Q(long_description__icontains=search_query) |
            models.Q(tags__icontains=search_query)
        )
    
    # Filter by category
    if category:
        blogs = blogs.filter(category__iexact=category)
    
    # Get all unique categories
    categories = BlogPost.objects.exclude(category__isnull=True).exclude(category='').values_list('category', flat=True).distinct()
    
    # Get featured posts
    featured_posts = blogs.filter(is_featured=True).order_by('-created_at')[:2]
    
    context = {
        'blogs': blogs,
        'featured_posts': featured_posts,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category,
    }
    return render(request, 'website/blog.html', context)


def blog_detail(request, slug):
    try:
        blog = BlogPost.objects.get(slug=slug)
        context = {'blog': blog}
        return render(request, 'website/blog_detail.html', context)
    except BlogPost.DoesNotExist:
        from django.http import Http404
        raise Http404("Blog post not found")


def team(request):
    team_members = TeamMember.objects.all()
    context = {'team_members': team_members}
    return render(request, 'website/team.html', context)


def services(request):
    return render(request, 'website/services.html')


def products(request):
    return render(request, 'website/products.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Here you can save to database or send email
            # For now, just show success message
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'website/contact.html', {'form': form})

