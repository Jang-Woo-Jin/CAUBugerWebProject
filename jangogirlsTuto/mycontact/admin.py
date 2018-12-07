from django.contrib import admin
from .models import User, Menu, Seat, Order, Notice

admin.site.register(User)
admin.site.register(Menu)
admin.site.register(Seat)
admin.site.register(Order)
admin.site.register(Notice)