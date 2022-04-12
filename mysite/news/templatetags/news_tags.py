from django import template

from news.models import Category

register = template.Library()


@register.simple_tag()
def categories_get():
    return Category.objects.all()