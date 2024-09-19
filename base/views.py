from django.shortcuts import render
from django.db import transaction, connection
import random
from .models import Product
import time
from django.http import JsonResponse

# Create your views here.

def update_product_price(request):
    product_id = 1
    new_price = random.randint(100 , 999)


    with transaction.atomic():
        product = Product.objects.get(id = product_id)
        current_version = product.version
        updated = Product.objects.filter(
            id = product.id,
            version = current_version
        ).update(
            price = new_price,
            version = current_version+1
        )

    return JsonResponse({
        "status" : True,
        "new_price" : new_price,

    })

def acquire_advisory_lock(lock_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT pg_advisory_lock(%s);", [lock_id])

def release_advisory_lock(lock_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT pg_advisory_unlock(%s);", [lock_id])

def update_product_price_with_lock(request):
    lock_id = 12345
    product_id = 1
    new_price = random.randint(100 , 999)
    try:
        acquire_advisory_lock(lock_id)
        print(f"Lock {lock_id} acquired!!!")
        time.sleep(10)
        with transaction.atomic():
            product = Product.objects.select_for_update().get(id = product_id)
            time.sleep(30)
            old_price = product.price
            product.price = new_price
            product.save() 

        return JsonResponse({
            "status" : True,
            "new_price" : new_price,
            "old_price" : old_price,

        })
    
    finally:
        release_advisory_lock(lock_id)
        print(f"Lock {lock_id} released!!!")

