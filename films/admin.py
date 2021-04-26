from django.contrib import admin
from .models import Film, Review, Essay, Comment

admin.site.register(Film)
admin.site.register(Review)
admin.site.register(Essay)
admin.site.register(Comment)