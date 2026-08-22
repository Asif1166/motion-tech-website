from django import template
import re

register = template.Library()


@register.filter(name='split')
def split(value, arg):
    """Split a string by the given argument"""
    if value:
        return value.split(arg)
    return []


@register.filter(name='trim')
def trim(value):
    """Trim whitespace from a string"""
    if value:
        return value.strip()
    return value


@register.filter(name='youtube_embed')
def youtube_embed(url):
    """Convert YouTube URL to embed URL"""
    if not url:
        return ''
    
    url = url.strip()
    
    # Ensure scheme
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'https://' + url
    
    # If it's already an embed url, return as-is
    if '/embed/' in url:
        return url
    
    # Short youtu.be links
    m = re.match(r'youtu\.be/([^\?&/]+)', url)
    if m:
        return f'https://www.youtube.com/embed/{m.group(1)}'
    
    # Standard watch?v=... links
    m = re.search(r'[?&]v=([^&]+)', url)
    if m:
        return f'https://www.youtube.com/embed/{m.group(1)}'
    
    # Last resort: try to extract last path segment as id
    m = re.search(r'youtube\.com/.*/([^\?&/]+)$', url)
    if m:
        return f'https://www.youtube.com/embed/{m.group(1)}'
    
    # Fallback
    return url

