from django import template


register = template.Library()


@register.filter
def get_mod(a, b):
    return str(a % b)
