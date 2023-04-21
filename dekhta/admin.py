from django.contrib import admin
from .models import Poets, Queries, Post
# Register your models here.

admin.site.register(Poets)
admin.site.register(Queries)
admin.site.register(Post)