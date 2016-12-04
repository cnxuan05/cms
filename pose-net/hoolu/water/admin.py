from django.contrib import admin
from django.contrib.auth.models import User
from water.models import *

# Register your models here.
admin.site.register(Author)
admin.site.register(AuthorDetail)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(News)


class ProfileInline(admin.StackedInline):
    model = UserProfile
    verbose_name = 'profile'


class UserAdmin(admin.ModelAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)

# admin.site.register(User)
admin.site.register(User, UserAdmin)
