from api.models import SiteSetting


def site_settings(request):
    """
    Context processor to provide site settings to all templates.
    """
    setting = SiteSetting.objects.first()
    if not setting:
        # Provide fallback defaults
        setting = SiteSetting(
            company_name='Motion Tech Ltd',
            site_title='Motion Tech Ltd - Software Development & IT Solutions',
            tagline='Crafting Digital Solutions That Businesses Trust',
            email='info@jatrasoft.com',
            phone='+8801601693138',
            address='123 Main Street, Dhaka, Bangladesh',
            whatsapp_number='8801601693138',
            calendly_url='https://calendly.com/hafizul-islam/30min',
            facebook_url='https://facebook.com',
            twitter_url='https://twitter.com',
            instagram_url='https://instagram.com',
            linkedin_url='https://linkedin.com',
            footer_about='Our mission is to deliver high-quality software solutions that empower businesses and individuals to achieve more with technology.',
            copyright_text='Motion Tech Ltd. All rights reserved.'
        )
    return {'site_settings': setting}

