from django.shortcuts import render
from .models import Category, Product

def home(request):
    owner_name = "Uttam F. Sisodia"
    company_details = {
        "name": "Selico Plastic",
        "established": "2017",
        "location": "Mumbai, Maharashtra, India",
        "nature": "Manufacturer",
        "gst_date": "01-07-2017",
        "legal_status": "Proprietorship"
    }
    
    return render(request, 'core/index.html', {
        'owner_name': owner_name,
        'company_details': company_details
    })

def categories_page(request):
    categories = Category.objects.prefetch_related('products').all()
    company_details = {
        "name": "Selico Plastic",
        "location": "Mumbai, Maharashtra, India",
    }
    return render(request, 'core/categories.html', {
        'categories': categories,
        'company_details': company_details
    })

def about_page(request):
    owner_name = "Uttam F. Sisodia"
    company_details = {
        "name": "Selico Plastic",
        "established": "2017",
        "location": "Mumbai, Maharashtra, India",
        "nature": "Manufacturer",
        "gst_date": "01-07-2017",
        "legal_status": "Proprietorship"
    }
    return render(request, 'core/about.html', {
        'owner_name': owner_name,
        'company_details': company_details
    })

def contact_page(request):
    company_details = {
        "name": "Selico Plastic",
        "location": "Mumbai, Maharashtra, India",
    }
    return render(request, 'core/contact.html', {
        'company_details': company_details
    })
