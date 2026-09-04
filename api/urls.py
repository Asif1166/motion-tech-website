from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, HeroSectionViewSet, AboutSectionViewSet,
    BlogPostViewSet, TeamMemberViewSet, TestimonialViewSet,
    ServiceViewSet, ProductViewSet, WhyChooseUsViewSet,
    CoreValueViewSet, TechStackViewSet, SiteSettingViewSet,
    ContactMessageViewSet, RegisterView, LoginView
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'HeroSection', HeroSectionViewSet, basename='herosection')
router.register(r'AboutSection', AboutSectionViewSet, basename='aboutsection')
router.register(r'BlogPosts', BlogPostViewSet, basename='blogpost')
router.register(r'TeamMembers', TeamMemberViewSet, basename='teammember')
router.register(r'Testimonials', TestimonialViewSet, basename='testimonial')
router.register(r'Services', ServiceViewSet, basename='service')
router.register(r'Products', ProductViewSet, basename='product')
router.register(r'WhyChooseUs', WhyChooseUsViewSet, basename='whychooseus')
router.register(r'CoreValues', CoreValueViewSet, basename='corevalue')
router.register(r'TechStacks', TechStackViewSet, basename='techstack')
router.register(r'SiteSettings', SiteSettingViewSet, basename='sitesetting')
router.register(r'ContactMessages', ContactMessageViewSet, basename='contactmessage')

urlpatterns = [
    path('', include(router.urls)),
    path('Auth/register', RegisterView.as_view(), name='register'),
    path('Auth/login', LoginView.as_view(), name='login'),
]

