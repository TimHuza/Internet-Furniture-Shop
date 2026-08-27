from goods.models import Category
from django import template

register = template.Library()


@register.simple_tag()
def tag_category():
    return Category.objects.all()