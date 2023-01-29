from django.contrib import admin
from .models import Review, Membership, Instructor, MembershipDetail, Payment, UserActivated

# Register your models here.


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "message", "date")


@admin.register(UserActivated)
class UserActivatedAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status")


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ("id", "user_account", "member_class", "phone", "program", "payment_status", "end", "active_status")


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address", "birth", "phone", "date", "schedule")


@admin.register(MembershipDetail)
class MembershipDetailAdmin(admin.ModelAdmin):
    list_display = ("id", "member_class", "price")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id_payment", "transaction_time", "gross_amount", "payment_type", "payment_status")
