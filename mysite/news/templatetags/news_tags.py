from django import template
from django.db.models import Count
from news.models import Category

register = template.Library()


@register.simple_tag()
def categories_get():
    return Category.objects.annotate(category__count=Count('news'))
