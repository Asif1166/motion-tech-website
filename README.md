# JatraSoft Website - Django Version

This is a Django clone of the .NET/Blazor website with the same database structure and design.

## Features

- ✅ Same database models (User, HeroSection, AboutSection, BlogPost, TeamMember, Testimonial)
- ✅ Same API endpoints
- ✅ Same frontend design using Django templates
- ✅ PostgreSQL database support
- ✅ JWT authentication
- ✅ Admin panel

## Setup Instructions

### 1. Install Dependencies

```bash
cd django_website
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Database Setup

Make sure PostgreSQL is running with the database `JatraSoftWeb`:

```bash
# Database should already exist from .NET project
# Host: localhost
# Port: 5432
# Database: JatraSoftWeb
# Username: postgres
# Password: 12345
```

### 3. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Admin User and Seed Data

```bash
python manage.py seed_data
```

This will:
- Create default admin user (username: `admin`, password: `admin123`)
- Load JSON data from `../Company_Website_Backend-main/db/` folder

### 5. Create Superuser (Optional - for Django admin)

```bash
python manage.py createsuperuser
```

### 6. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 7. Run the Server

```bash
python manage.py runserver
```

The website will be available at:
- Frontend: http://localhost:8000
- API: http://localhost:8000/api/
- Admin: http://localhost:8000/admin/

## API Endpoints

All endpoints match the .NET version:

- `GET /api/HeroSection/` - List hero sections
- `GET /api/AboutSection/` - List about sections
- `GET /api/BlogPosts/` - List blog posts
- `GET /api/BlogPosts/featured/` - Featured blog posts
- `GET /api/BlogPosts/slug/{slug}/` - Get blog by slug
- `GET /api/TeamMembers/` - List team members
- `GET /api/Testimonials/` - List testimonials
- `POST /api/Auth/register` - Register user
- `POST /api/Auth/login` - Login user

## Project Structure

```
django_website/
├── api/                    # API app (models, views, serializers)
│   ├── models.py          # Database models
│   ├── views.py           # API viewsets
│   ├── serializers.py     # DRF serializers
│   └── management/
│       └── commands/
│           └── seed_data.py  # Data seeding command
├── website/                # Website app (templates, views)
│   ├── views.py           # Template views
│   └── urls.py            # URL routing
├── templates/              # Django templates
│   ├── base.html          # Base template
│   └── website/           # Page templates
├── static/                 # Static files (CSS, JS, images)
│   ├── css/               # CSS files
│   └── Assets/            # Images
├── jatrasoft_website/     # Project settings
│   ├── settings.py        # Django settings
│   └── urls.py            # Main URL config
└── manage.py              # Django management script
```

## Copy Static Files

You need to copy CSS and image files from the Blazor project:

```bash
# Copy CSS files
cp -r ../Company_Website_Frontend-main/ClientSite/wwwroot/css static/

# Copy Assets
cp -r ../Company_Website_Frontend-main/ClientSite/wwwroot/Assets static/
```

## Default Admin Credentials

- Username: `admin`
- Password: `admin123`

**⚠️ Change the password after first login!**

## Notes

- The database tables use different names (prefixed with `api_`) but have the same structure
- JWT tokens are compatible with the .NET version
- All API endpoints match the .NET version for compatibility

