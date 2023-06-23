from django.contrib import admin
from myapp.models import news_db
# Register your models here.


class news_upload(admin.ModelAdmin):
    list_display = ("title", "date", "author","content")

admin.site.register(news_db, news_upload)