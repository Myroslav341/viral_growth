from django import template

register = template.Library()


@register.filter
def get_mod(a, b):
    return str(int(a) % int(b))
