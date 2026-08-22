from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, HeroSectionViewSet, AboutSectionViewSet,
    BlogPostViewSet, TeamMemberViewSet, TestimonialViewSet,
    RegisterView, LoginView
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'HeroSection', HeroSectionViewSet, basename='herosection')
router.register(r'AboutSection', AboutSectionViewSet, basename='aboutsection')
router.register(r'BlogPosts', BlogPostViewSet, basename='blogpost')
router.register(r'TeamMembers', TeamMemberViewSet, basename='teammember')
router.register(r'Testimonials', TestimonialViewSet, basename='testimonial')

urlpatterns = [
    path('', include(router.urls)),
    path('Auth/register', RegisterView.as_view(), name='register'),
    path('Auth/login', LoginView.as_view(), name='login'),
]

