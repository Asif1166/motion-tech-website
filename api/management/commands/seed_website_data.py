from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import (
    User, HeroSection, AboutSection, BlogPost, TeamMember, Testimonial,
    Service, Product, WhyChooseUs, CoreValue, TechStack, SiteSetting
)


class Command(BaseCommand):
    help = 'Seeds all website sections with rich initial data'

    def handle(self, *args, **options):
        with transaction.atomic():
            # 1. Admin User
            if not User.objects.filter(username='admin').exists():
                admin_user = User(username='admin', role='Admin')
                admin_user.set_password('admin123')
                admin_user.save()
                self.stdout.write(self.style.SUCCESS('✓ Created admin user: admin / admin123'))

            # 2. Site Setting
            site_setting, created = SiteSetting.objects.get_or_create(
                id=1,
                defaults={
                    'company_name': 'Motion Tech Ltd',
                    'site_title': 'Motion Tech Ltd - Software Development & IT Solutions',
                    'tagline': 'Crafting Digital Solutions That Businesses Trust',
                    'email': 'info@jatrasoft.com',
                    'phone': '+8801601693138',
                    'address': '123 Main Street, Dhaka, Bangladesh',
                    'whatsapp_number': '8801601693138',
                    'calendly_url': 'https://calendly.com/hafizul-islam/30min',
                    'facebook_url': 'https://facebook.com',
                    'twitter_url': 'https://twitter.com',
                    'instagram_url': 'https://instagram.com',
                    'linkedin_url': 'https://linkedin.com',
                    'github_url': 'https://github.com',
                    'footer_about': 'Our mission is to deliver high-quality software solutions that empower businesses and individuals to achieve more with technology.',
                    'copyright_text': 'Motion Tech Ltd. All rights reserved.',
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS('✓ Created SiteSetting'))

            # 3. Hero Section
            if not HeroSection.objects.exists():
                HeroSection.objects.create(
                    title='Crafting Digital Solutions That Businesses Trust',
                    subtitle='Innovative Technology & Software Development Partner',
                    short_description='We build modern, scalable web, mobile, and enterprise applications tailored to your business needs with cutting-edge technologies.',
                    experience_stat='4+ Years',
                    projects_stat='100+ Projects',
                    clients_stat='50+ Clients',
                    primary_btn_text='Get Started',
                    primary_btn_url='/services/',
                    secondary_btn_text='Contact Us',
                    secondary_btn_url='/contact/'
                )
                self.stdout.write(self.style.SUCCESS('✓ Created HeroSection'))

            # 4. About Section
            about_section = AboutSection.objects.first()
            if not about_section:
                about_section = AboutSection.objects.create(
                    title='Empowering Businesses Through Modern Technology',
                    description='Motion Tech Ltd was founded with a singular focus to transform challenging business problems into elegant, scalable, and intuitive digital solutions. Since our inception, we have partnered with over 50+ clients globally, delivering more than 100 innovative projects across various industries, from FinTech to E-commerce. We are driven by a passion for technology and a deep commitment to our clients\' success, treating every engagement as the beginning of a shared journey.',
                    video_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                    journey_subtitle='OUR JOURNEY SO FAR',
                    journey_title='Building the Digital Future with Motion Tech',
                    journey_description='Motion Tech Ltd was founded in 2024 with a singular focus to transform challenging business problems into elegant, scalable, and intuitive digital solutions. Since our inception, we have partnered with over 50+ clients globally, delivering more than 100 innovative projects across various industries, from FinTech to E-commerce. We are driven by a passion for technology and a deep commitment to our clients\' success, treating every engagement as the beginning of a shared journey.',
                    mission_title='Our Mission',
                    mission_description='To empower businesses with innovative, reliable, and scalable software solutions that accelerate growth, improve efficiency, and deliver exceptional user experiences.',
                    vision_title='Our Vision',
                    vision_description='To become a leading global technology company recognized for excellence in innovation, quality, and customer success—building digital solutions that shape the future.',
                    stat_experience='4+',
                    stat_projects='100+',
                    stat_clients='50+'
                )
                self.stdout.write(self.style.SUCCESS('✓ Created AboutSection'))
            else:
                # Update stats and mission/vision if blank
                if not about_section.mission_description:
                    about_section.journey_subtitle = 'OUR JOURNEY SO FAR'
                    about_section.journey_title = 'Building the Digital Future with Motion Tech'
                    about_section.journey_description = 'Motion Tech Ltd was founded in 2024 with a singular focus to transform challenging business problems into elegant, scalable, and intuitive digital solutions. Since our inception, we have partnered with over 50+ clients globally, delivering more than 100 innovative projects across various industries, from FinTech to E-commerce.'
                    about_section.mission_title = 'Our Mission'
                    about_section.mission_description = 'To empower businesses with innovative, reliable, and scalable software solutions that accelerate growth, improve efficiency, and deliver exceptional user experiences.'
                    about_section.vision_title = 'Our Vision'
                    about_section.vision_description = 'To become a leading global technology company recognized for excellence in innovation, quality, and customer success—building digital solutions that shape the future.'
                    about_section.stat_experience = '4+'
                    about_section.stat_projects = '100+'
                    about_section.stat_clients = '50+'
                    about_section.save()
                    self.stdout.write(self.style.SUCCESS('✓ Updated existing AboutSection with rich fields'))

            # 5. Core Values
            if not CoreValue.objects.exists():
                core_values_data = [
                    {
                        'title': 'Innovation',
                        'description': 'We constantly seek new technologies and creative approaches to solve complex problems.',
                        'icon': 'bi bi-lightbulb-fill',
                        'icon_color': '#0099FF',
                        'stat_class': 'base-stat-1',
                        'order': 1
                    },
                    {
                        'title': 'Integrity',
                        'description': 'Honesty and transparency are the foundations of all our client relationships.',
                        'icon': 'bi bi-hand-thumbs-up-fill',
                        'icon_color': '#555555',
                        'stat_class': 'base-stat-2',
                        'order': 2
                    },
                    {
                        'title': 'Excellence',
                        'description': 'We strive for the highest quality in code, design, and user experience delivery.',
                        'icon': 'bi bi-rocket-takeoff-fill',
                        'icon_color': '#0d6efd',
                        'stat_class': 'base-stat-3',
                        'order': 3
                    },
                ]
                for cv in core_values_data:
                    CoreValue.objects.create(**cv)
                self.stdout.write(self.style.SUCCESS(f'✓ Created {len(core_values_data)} CoreValues'))

            # 6. Services
            if not Service.objects.exists():
                services_data = [
                    {
                        'title': 'Web Development',
                        'slug': 'web-development',
                        'icon': 'bi bi-code-slash',
                        'icon_color': '#0d6efd',
                        'short_description': 'Launch a modern, responsive website tailored to your brand. Sleek, fast-loading sites built for growth.',
                        'full_description': 'Our web development services provide end-to-end solutions using modern frameworks like React, Django, Next.js, and Node.js. We build performant, SEO-optimized, and secure web applications.',
                        'order': 1,
                    },
                    {
                        'title': 'E-commerce',
                        'slug': 'e-commerce',
                        'icon': 'bi bi-cart-check',
                        'icon_color': '#198754',
                        'short_description': 'Sell online with ease! Secure, user-friendly stores with payments, inventory, and order management.',
                        'full_description': 'We create robust eCommerce platforms featuring multi-currency support, seamless checkout flows, secure payment gateways, inventory sync, and intelligent analytics.',
                        'order': 2,
                    },
                    {
                        'title': 'App Development',
                        'slug': 'app-development',
                        'icon': 'bi bi-phone',
                        'icon_color': '#ffc107',
                        'short_description': 'Create high-performance mobile apps for Android and iOS that look great and run smoothly.',
                        'full_description': 'Native and cross-platform mobile apps built with Flutter, React Native, Swift, and Kotlin. We ensure fluid animations, offline capabilities, and cloud synchronisation.',
                        'order': 3,
                    },
                    {
                        'title': 'Game Development',
                        'slug': 'game-development',
                        'icon': 'bi bi-controller',
                        'icon_color': '#dc3545',
                        'short_description': 'Turn your game idea into reality with creative 2D & 3D experiences optimized for performance and fun.',
                        'full_description': 'From concept to publishing, we craft immersive gaming experiences across platforms using Unity, Unreal Engine, and WebGL.',
                        'order': 4,
                    },
                    {
                        'title': 'Digital Marketing',
                        'slug': 'digital-marketing',
                        'icon': 'bi bi-bullseye',
                        'icon_color': '#0dcaf0',
                        'short_description': 'Grow your brand with SEO, content, ads, and social strategies designed to attract and convert your audience.',
                        'full_description': 'Comprehensive digital growth strategies including search engine optimization (SEO), PPC campaigns, email marketing, and conversion rate optimization.',
                        'order': 5,
                    },
                    {
                        'title': 'ERP Software',
                        'slug': 'erp-software',
                        'icon': 'bi bi-building-gear',
                        'icon_color': '#6610f2',
                        'short_description': 'Simplify operations with custom ERP systems — manage HR, sales, and inventory all in one smart solution.',
                        'full_description': 'Enterprise Resource Planning systems built from the ground up to fit your operational workflows, reporting needs, and organizational hierarchy.',
                        'order': 6,
                    },
                ]
                for s in services_data:
                    Service.objects.create(**s)
                self.stdout.write(self.style.SUCCESS(f'✓ Created {len(services_data)} Services'))

            # 7. Products
            if not Product.objects.exists():
                products_data = [
                    {
                        'title': 'HRMS',
                        'slug': 'hrms-software',
                        'category_tag': 'hrms',
                        'icon': 'bi bi-people-fill',
                        'icon_color': '#2E7D32',
                        'short_description': 'HR operations — attendance, payroll, performance tracking, and employee self-service portal.',
                        'full_description': 'Comprehensive Human Resource Management System designed to automate employee lifecycle management, attendance tracking with biometric integration, payroll generation, and leave approvals.',
                        'demo_url': '/contact/',
                        'order': 1,
                    },
                    {
                        'title': 'CRM',
                        'slug': 'crm-solution',
                        'category_tag': 'crm',
                        'icon': 'bi bi-bar-chart-fill',
                        'icon_color': '#EF6C00',
                        'short_description': 'Manage leads, clients, and sales pipelines with smart automation and actionable insights.',
                        'full_description': 'Customer Relationship Management solution that boosts conversion rates, organizes deal pipelines, tracks communications, and provides real-time sales forecasting.',
                        'demo_url': '/contact/',
                        'order': 2,
                    },
                    {
                        'title': 'POS System',
                        'slug': 'pos-system',
                        'category_tag': 'pos',
                        'icon': 'bi bi-cash-stack',
                        'icon_color': '#1E88E5',
                        'short_description': 'Handle sales, inventory, and real-time billing reporting efficiently across multiple stores.',
                        'full_description': 'Lightning-fast Point of Sale system suitable for retail and hospitality, supporting barcode scanning, thermal printing, multi-store stock management, and cashier shifts.',
                        'demo_url': '/contact/',
                        'order': 3,
                    },
                    {
                        'title': 'ERP Solution',
                        'slug': 'enterprise-erp',
                        'category_tag': 'erp',
                        'icon': 'bi bi-building-check',
                        'icon_color': '#8E24AA',
                        'short_description': 'Connect HR, finance, sales & inventory in one unified, modular enterprise suite.',
                        'full_description': 'All-in-one ERP platform that eliminates data silos across departments, providing executive dashboards, financial auditing, supply chain management, and automated alerts.',
                        'demo_url': '/contact/',
                        'order': 4,
                    },
                ]
                for p in products_data:
                    Product.objects.create(**p)
                self.stdout.write(self.style.SUCCESS(f'✓ Created {len(products_data)} Products'))

            # 8. Why Choose Us
            if not WhyChooseUs.objects.exists():
                why_data = [
                    {
                        'title': 'Custom Software',
                        'description': 'We build tailor-made applications to solve your specific business challenges with precision.',
                        'icon': 'bi bi-laptop',
                        'icon_color': 'text-primary',
                        'order': 1,
                    },
                    {
                        'title': 'Experienced Team',
                        'description': 'Our engineers bring deep technical expertise and industry experience to every project.',
                        'icon': 'bi bi-award',
                        'icon_color': 'text-success',
                        'order': 2,
                    },
                    {
                        'title': 'Scalable Solutions',
                        'description': 'We develop robust systems that grow seamlessly with your business needs and traffic.',
                        'icon': 'bi bi-graph-up-arrow',
                        'icon_color': 'text-warning',
                        'order': 3,
                    },
                    {
                        'title': '24/7 Support',
                        'description': 'Our dedicated support team is available around the clock to assist you and maintain uptime.',
                        'icon': 'bi bi-headset',
                        'icon_color': 'text-danger',
                        'order': 4,
                    },
                    {
                        'title': 'Creative Ideas',
                        'description': 'We turn innovative ideas into practical, engaging, and profitable digital solutions.',
                        'icon': 'bi bi-lightbulb',
                        'icon_color': 'text-info',
                        'order': 5,
                    },
                    {
                        'title': 'Fastest Delivery',
                        'description': 'We ensure agile and timely delivery without compromising on code quality and performance.',
                        'icon': 'bi bi-lightning-charge',
                        'icon_color': 'text-warning',
                        'order': 6,
                    },
                ]
                for w in why_data:
                    WhyChooseUs.objects.create(**w)
                self.stdout.write(self.style.SUCCESS(f'✓ Created {len(why_data)} WhyChooseUs features'))

            # 9. Tech Stacks
            if not TechStack.objects.exists():
                tech_data = [
                    {
                        'name': 'Frontend & UI',
                        'technologies': 'React, Angular, Vue.js, Next.js, Tailwind CSS, Bootstrap',
                        'icon': 'bi bi-laptop',
                        'order': 1,
                    },
                    {
                        'name': 'Backend & API',
                        'technologies': 'Python (Django/FastAPI), .NET Core, Node.js (Express), Java (Spring Boot)',
                        'icon': 'bi bi-server',
                        'order': 2,
                    },
                    {
                        'name': 'Mobile & Cross-Platform',
                        'technologies': 'Flutter, React Native, Swift (iOS Native), Kotlin (Android Native)',
                        'icon': 'bi bi-phone',
                        'order': 3,
                    },
                    {
                        'name': 'Cloud & Data',
                        'technologies': 'AWS, Google Cloud, Docker, Kubernetes, PostgreSQL, MySQL, Redis, MongoDB',
                        'icon': 'bi bi-cloud-check',
                        'order': 4,
                    },
                ]
                for t in tech_data:
                    TechStack.objects.create(**t)
                self.stdout.write(self.style.SUCCESS(f'✓ Created {len(tech_data)} TechStacks'))

            # 10. Team Members
            if not TeamMember.objects.exists():
                team_data = [
                    {
                        'name': 'Engr. Hafizul Islam',
                        'role': 'Founder & Lead Architect',
                        'bio': 'Over 8 years of experience building enterprise-grade architectures and leading cross-functional engineering teams.',
                        'facebook_url': 'https://facebook.com',
                        'linkedin_url': 'https://linkedin.com',
                        'github_url': 'https://github.com',
                        'order': 1,
                        'is_featured': True,
                    },
                    {
                        'name': 'Tanvir Ahmed',
                        'role': 'Senior Full-Stack Engineer',
                        'bio': 'Specializes in Python, Django, React, and building high-performance RESTful APIs.',
                        'facebook_url': 'https://facebook.com',
                        'linkedin_url': 'https://linkedin.com',
                        'github_url': 'https://github.com',
                        'order': 2,
                        'is_featured': True,
                    },
                    {
                        'name': 'Nusrat Jahan',
                        'role': 'UI/UX Designer & Frontend Dev',
                        'bio': 'Passionate about crafting intuitive, accessible, and delightful digital user experiences.',
                        'instagram_url': 'https://instagram.com',
                        'linkedin_url': 'https://linkedin.com',
                        'order': 3,
                        'is_featured': True,
                    },
                    {
                        'name': 'Sabbir Hossain',
                        'role': 'Mobile App Developer',
                        'bio': 'Flutter & Android specialist with a track record of deploying popular consumer and B2B apps.',
                        'facebook_url': 'https://facebook.com',
                        'linkedin_url': 'https://linkedin.com',
                        'github_url': 'https://github.com',
                        'order': 4,
                        'is_featured': True,
                    },
                    {
                        'name': 'Afsana Mim',
                        'role': 'QA & Project Manager',
                        'bio': 'Ensures high quality standards, automated test coverage, and smooth client deliverables on time.',
                        'linkedin_url': 'https://linkedin.com',
                        'order': 5,
                        'is_featured': True,
                    },
                    {
                        'name': 'Mahmudul Hasan',
                        'role': 'DevOps & Cloud Engineer',
                        'bio': 'Manages CI/CD pipelines, Docker containers, AWS/GCP clusters, and database high-availability.',
                        'github_url': 'https://github.com',
                        'linkedin_url': 'https://linkedin.com',
                        'order': 6,
                        'is_featured': True,
                    },
                ]
                for tm in team_data:
                    TeamMember.objects.create(**tm)
                self.stdout.write(self.style.SUCCESS(f'✓ Created {len(team_data)} TeamMembers'))

            # 11. Testimonials
            if not Testimonial.objects.exists():
                test_data = [
                    {
                        'client_name': 'Rashidul Karim',
                        'company_name': 'Apex Retailers',
                        'quote': 'Motion Tech delivered our POS and inventory system well ahead of schedule. Our daily checkout speed increased by 40% and inventory errors dropped to zero.',
                        'rating': 5,
                        'order': 1,
                        'is_published': True,
                    },
                    {
                        'client_name': 'Sarah Jenkins',
                        'company_name': 'Global Logistics Inc.',
                        'quote': 'The custom ERP system they built transformed how we handle freight forwarding and client reporting. Truly a dependable technology partner!',
                        'rating': 5,
                        'order': 2,
                        'is_published': True,
                    },
                    {
                        'client_name': 'Farhan Chowdhury',
                        'company_name': 'Dhaka FinTech Labs',
                        'quote': 'Outstanding mobile app development team. They built our Flutter app with fantastic animations and bulletproof security. Highly recommended!',
                        'rating': 5,
                        'order': 3,
                        'is_published': True,
                    },
                ]
                for t in test_data:
                    Testimonial.objects.create(**t)
                self.stdout.write(self.style.SUCCESS(f'✓ Created {len(test_data)} Testimonials'))

            # 12. Sample Blog Posts
            if not BlogPost.objects.exists():
                blog_data = [
                    {
                        'title': 'How Modern ERP Systems Drive Business Growth in 2026',
                        'slug': 'how-modern-erp-systems-drive-business-growth',
                        'short_description': 'Discover how integrating your HR, inventory, and finance processes into a single ERP platform cuts operational costs.',
                        'long_description': '<p>Enterprise resource planning (ERP) systems have evolved rapidly. In 2026, modern cloud-based ERP solutions offer unprecedented modularity and ease of integration...</p>',
                        'category': 'Enterprise',
                        'tags': 'ERP, Business, Technology',
                        'author_name': 'Tanvir Ahmed',
                        'read_time_minutes': 5,
                        'is_featured': True,
                    },
                    {
                        'title': 'Choosing the Right Tech Stack for Your Next Mobile App',
                        'slug': 'choosing-right-tech-stack-mobile-app',
                        'short_description': 'Flutter vs React Native vs Native: Which technology is best suited for your startup in terms of cost and speed?',
                        'long_description': '<p>Building a mobile app requires strategic architectural decisions early on. Here is our comprehensive comparison of cross-platform versus native development...</p>',
                        'category': 'Mobile',
                        'tags': 'Flutter, Mobile, iOS, Android',
                        'author_name': 'Sabbir Hossain',
                        'read_time_minutes': 6,
                        'is_featured': True,
                    },
                ]
                for b in blog_data:
                    BlogPost.objects.create(**b)
                self.stdout.write(self.style.SUCCESS(f'✓ Created {len(blog_data)} sample BlogPosts'))

        self.stdout.write(self.style.SUCCESS('🎉 All website data successfully seeded!'))

