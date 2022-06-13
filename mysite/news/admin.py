from django.contrib import admin
from news.models import News, Category
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class MyModel_Admin(admin.ModelAdmin):
    list_display = ('id', 'caption', "category", "created_at", "updated_at", "is_published")
    list_display_links = ('id', 'caption')
    search_fields = ('caption', 'text')
    list_filter = ("is_published", "category")
    list_editable = ("is_published", "category")


class Category_Admin(admin.ModelAdmin):
    list_display = ('id', "category")
    list_display_links = ('id', 'category')
    search_fields = ('category',)


class CustomUser_Admin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', "photo", "gender"]


admin.site.register(News, MyModel_Admin)
admin.site.register(Category, Category_Admin)
admin.site.register(CustomUser, CustomUser_Admin)
