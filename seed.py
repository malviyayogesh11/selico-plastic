import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'selicoweb.settings')
django.setup()

from core.models import Category, Product

# Categories from the provided Indiamart link
categories_data = [
    "Plastic Container",
    "Plastic Box",
    "Plastic Lunch Box",
    "Plastic Bowl",
    "Plastic Glass",
    "Plastic Sweet Box",
    "Ice Cream Container",
    "Plastic Packing Box",
    "Plastic Soap Case"
]

products_data = [
    {"category": "Plastic Container", "name": "Kimia Dates Box", "price": 120.00, "image_url": "https://5.imimg.com/data5/IK/NK/MY-4428719/kimia-dates-box-500x500.jpg"},
    {"category": "Plastic Lunch Box", "name": "Kids Plastic Lunch Box", "price": 250.00, "image_url": "https://5.imimg.com/data5/SM/CR/MY-4428719/kids-plastic-lunch-box-250x250.jpg"},
    {"category": "Plastic Bowl", "name": "Premium Bowl Set", "price": 350.00, "image_url": "https://5.imimg.com/data5/FI/LS/MY-4428719/plastic-bowl-250x250.jpg"},
    {"category": "Ice Cream Container", "name": "Ice Cream Tub", "price": 180.00, "image_url": "https://5.imimg.com/data5/BR/CF/MY-4428719/ice-cream-tub-250x250.jpg"},
    {"category": "Plastic Container", "name": "Yogurt Plastic Packaging Cup", "price": 90.00, "image_url": "https://5.imimg.com/data5/SELLER/Default/2026/4/598537325/TO/SV/MH/4428719/yogurt-plastic-packaging-cup-250x250.png"},
    {"category": "Plastic Sweet Box", "name": "Laddu And Sweet Plastic Box", "price": 80.00, "image_url": "https://5.imimg.com/data5/SELLER/Default/2024/7/439339437/MO/QJ/NA/4428719/sb1000-500x500.jpg"},
    {"category": "Plastic Box", "name": "Keeper 88 Plastic Box", "price": 90.00, "image_url": "https://5.imimg.com/data5/SELLER/Default/2022/5/AZ/UP/NF/4428719/dsc-1081-250x250.jpg"},
    {"category": "Plastic Container", "name": "Elegant Plastic Serving Tray", "price": 150.00, "image_url": "https://5.imimg.com/data5/LT/AP/MY-4428719/elegant-plastic-serving-tray-250x250.jpg"},
    {"category": "Plastic Glass", "name": "Lemon Juice Set", "price": 200.00, "image_url": "https://4.imimg.com/data4/PB/WQ/MY-4428719/lemon-juice-set-250x250.jpg"},
    {"category": "Plastic Container", "name": "Dates Packing Container", "price": 100.00, "image_url": "https://5.imimg.com/data5/SELLER/Default/2026/4/598533431/SH/DN/EG/4428719/dates-packing-plastic-container-250x250.png"},
    {"category": "Plastic Box", "name": "Powder Case", "price": 60.00, "image_url": "https://3.imimg.com/data3/OO/YR/MY-4428719/powder-case-250x250.jpg"},
    {"category": "Plastic Container", "name": "Plastic Food Container", "price": 120.00, "image_url": "https://5.imimg.com/data5/SELLER/Default/2025/6/521409298/LG/KI/CY/4428719/plastic-food-container-250x250.jpg"},
    {"category": "Plastic Container", "name": "Plastic Jug", "price": 180.00, "image_url": "https://5.imimg.com/data5/KK/WN/MY-4428719/plastic-jug-250x250.jpg"},
    {"category": "Plastic Glass", "name": "Plastic Juice Glass", "price": 40.00, "image_url": "https://5.imimg.com/data5/SELLER/Default/2020/10/VV/DY/LK/4428719/plastic-juice-glass-250x250.jpg"},
]

def run():
    print("Seeding database...")
    for cat_name in categories_data:
        Category.objects.get_or_create(name=cat_name)
    
    # Delete old products to refresh with real images
    Product.objects.all().delete()
    
    for prod in products_data:
        cat = Category.objects.get(name=prod['category'])
        Product.objects.create(
            name=prod['name'],
            category=cat,
            price=prod['price'],
            image_url=prod['image_url']
        )
    print("Database seeded successfully!")

if __name__ == '__main__':
    run()
