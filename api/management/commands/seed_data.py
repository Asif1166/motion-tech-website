import json
import os
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import HeroSection, AboutSection, User
import bcrypt


class Command(BaseCommand):
    help = 'Seed data from JSON files and create admin user'

    def add_arguments(self, parser):
        parser.add_argument(
            '--db-path',
            type=str,
            default='../Company_Website_Backend-main/db',
            help='Path to the db folder containing JSON files'
        )

    def handle(self, *args, **options):
        db_path = options['db_path']
        
        with transaction.atomic():
            # Create admin user if none exists
            if not User.objects.exists():
                admin_user = User(username='admin', role='Admin')
                admin_user.set_password('admin123')
                admin_user.save()
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Created admin user: admin / admin123')
                )
            else:
                self.stdout.write('Users already exist, skipping admin user creation')
            
            # Seed HeroSection
            if not HeroSection.objects.exists():
                json_file = os.path.join(db_path, 'response_1766385618795.json')
                if os.path.exists(json_file):
                    with open(json_file, 'r') as f:
                        data = json.load(f)
                        for item in data:
                            HeroSection.objects.create(
                                title=item.get('title', ''),
                                short_description=item.get('shortDescription', '')
                                # Note: image field needs to be uploaded via admin or API
                            )
                        self.stdout.write(
                            self.style.SUCCESS(f'✓ Loaded {len(data)} HeroSection(s) (images need to be uploaded separately)')
                        )
            
            # Seed AboutSection
            if not AboutSection.objects.exists():
                json_file = os.path.join(db_path, 'response_1766385561226.json')
                if os.path.exists(json_file):
                    with open(json_file, 'r') as f:
                        data = json.load(f)
                        for item in data:
                            AboutSection.objects.create(
                                title=item.get('title', ''),
                                description=item.get('description', ''),
                                video_url=item.get('videoUrl', '')
                                # Note: image field needs to be uploaded via admin or API
                            )
                        self.stdout.write(
                            self.style.SUCCESS(f'✓ Loaded {len(data)} AboutSection(s) (images need to be uploaded separately)')
                        )
        
        self.stdout.write(self.style.SUCCESS('✓ Data seeding completed!'))

