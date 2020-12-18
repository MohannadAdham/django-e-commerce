from django.contrib import admin

from .models import User, Listing, Bid, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Listing)

# class ListingAdmin(admin.ModelAdmin):
#     list_display = ("id", "title", "price", "creation_date")


admin.site.register(Bid)
admin.site.register(Comment)