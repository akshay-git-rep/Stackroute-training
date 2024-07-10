from django.contrib import admin
from profiles_api.models import Post, UserProfile, Book, ProfileFeedItem, Laptop

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Book)
admin.site.register(Post)
admin.site.register(ProfileFeedItem)
admin.site.register(Laptop)

# register laptop model for admin
