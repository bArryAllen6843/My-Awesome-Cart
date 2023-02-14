from django.contrib import admin

# Register your models here.
from .models import Product, Contact, Orders, OrderUpdate

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)

# to change admin password type in terminal
# python manage.py changepassword aayush(username)