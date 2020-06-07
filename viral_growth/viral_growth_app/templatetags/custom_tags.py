from django import template


register = template.Library()


@register.filter
def get_mod(a, b):
    """
    template tag for mod handle
    """
    return str(a % b)
