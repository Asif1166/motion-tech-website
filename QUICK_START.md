# Django Website - Quick Start

## 🚀 Quick Setup

### 1. Install and Setup

```bash
cd django_website
bash setup.sh
```

### 2. Copy Static Files

```bash
# Copy CSS files
cp -r ../Company_Website_Frontend-main/ClientSite/wwwroot/css static/

# Copy Assets (images)
cp -r ../Company_Website_Frontend-main/ClientSite/wwwroot/Assets static/
```

### 3. Run Server

```bash
source venv/bin/activate
python manage.py runserver
```

### 4. Access

- **Frontend**: http://localhost:8000
- **API**: http://localhost:8000/api/
- **Admin Panel**: http://localhost:8000/admin/

## 📋 Default Credentials

- **Username**: `admin`
- **Password**: `admin123`

## ✅ What's Included

- ✅ Same database models as .NET version
- ✅ Same API endpoints
- ✅ Same frontend design
- ✅ PostgreSQL database
- ✅ JWT authentication
- ✅ Admin panel

## 🔧 Manual Setup (if setup.sh doesn't work)

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Seed data
python manage.py seed_data

# Collect static files
python manage.py collectstatic --noinput

# Run server
python manage.py runserver
```

## 📝 Notes

- Uses the same PostgreSQL database (`JatraSoftWeb`)
- API endpoints match the .NET version
- Templates use the same CSS and design

