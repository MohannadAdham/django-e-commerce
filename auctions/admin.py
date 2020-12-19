from django.contrib import admin

from .models import User, Listing, Bid, Comment

# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "creation_date")

class BidAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "listing", "amount", "bid_date")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "listing", "content")

admin.site.register(User)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Comment, CommentAdmin)
