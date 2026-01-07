from django import template

register = template.Library()

@register.filter
def split(value, delimiter=','):
    """
    Splits a string by the given delimiter and returns a list.
    Usage: {{ my_string|split:"," }}
    """
    return value.split(delimiter)