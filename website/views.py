from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import models
from api.models import (
    HeroSection, AboutSection, BlogPost, TeamMember, Testimonial,
    Service, Product, WhyChooseUs, CoreValue, TechStack, ContactMessage
)
from .forms import ContactForm


def home(request):
    heroes = HeroSection.objects.all()[:1]
    about = AboutSection.objects.first()
    services = Service.objects.filter(is_active=True)
    products = Product.objects.filter(is_active=True)
    why_choose_us = WhyChooseUs.objects.filter(is_active=True)
    blogs = BlogPost.objects.all().order_by('-created_at')[:6]
    
    # Featured team members or all if not set
    team_members = TeamMember.objects.filter(is_featured=True)
    if not team_members.exists():
        team_members = TeamMember.objects.all()[:6]
    else:
        team_members = team_members[:6]

    testimonials = Testimonial.objects.filter(is_published=True)
    
    context = {
        'heroes': heroes,
        'about': about,
        'services': services,
        'products': products,
        'why_choose_us': why_choose_us,
        'blogs': blogs,
        'team_members': team_members,
        'testimonials': testimonials,
    }
    return render(request, 'website/home.html', context)


def about(request):
    about = AboutSection.objects.first()
    core_values = CoreValue.objects.filter(is_active=True)
    why_choose_us = WhyChooseUs.objects.filter(is_active=True)
    products = Product.objects.filter(is_active=True)
    team_members = TeamMember.objects.all()
    testimonials = Testimonial.objects.filter(is_published=True)

    context = {
        'about': about,
        'core_values': core_values,
        'why_choose_us': why_choose_us,
        'products': products,
        'team_members': team_members,
        'testimonials': testimonials,
    }
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
    services_list = Service.objects.filter(is_active=True)
    tech_stacks = TechStack.objects.all()
    context = {
        'services': services_list,
        'tech_stacks': tech_stacks,
    }
    return render(request, 'website/services.html', context)


def products(request):
    products_list = Product.objects.filter(is_active=True)
    context = {
        'products': products_list,
    }
    return render(request, 'website/products.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'website/contact.html', {'form': form})

