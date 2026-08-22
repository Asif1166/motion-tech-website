#!/bin/bash

echo "=========================================="
echo "Django Website Setup"
echo "=========================================="
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed!"
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

echo ""
echo "Activating virtual environment..."
source venv/bin/activate

echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "Running migrations..."
python manage.py makemigrations
python manage.py migrate

echo ""
echo "Seeding data..."
python manage.py seed_data

echo ""
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo ""
echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Copy static files:"
echo "   cp -r ../Company_Website_Frontend-main/ClientSite/wwwroot/css static/"
echo "   cp -r ../Company_Website_Frontend-main/ClientSite/wwwroot/Assets static/"
echo ""
echo "2. Run the server:"
echo "   source venv/bin/activate"
echo "   python manage.py runserver"
echo ""
echo "3. Access:"
echo "   Frontend: http://localhost:8000"
echo "   API: http://localhost:8000/api/"
echo "   Admin: http://localhost:8000/admin/"
echo ""
echo "Default admin: admin / admin123"
echo ""

