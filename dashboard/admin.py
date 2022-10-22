from django.contrib import admin
from .models import Review, Membership, Instructor

# Register your models here.
admin.site.register(Review)
admin.site.register(Membership)
admin.site.register(Instructor)
