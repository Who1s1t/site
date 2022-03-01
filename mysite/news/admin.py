from django.contrib import admin
from news.models import MyModel, Category


# Register your models here.
class MyModel_Admin(admin.ModelAdmin):
    list_display = ('id', 'caption', "created_at", "updated_at", "is_published")
    list_display_links = ('id', 'caption')
    search_fields = ('caption', 'text')


admin.site.register(MyModel, MyModel_Admin)
admin.site.register(Category)
