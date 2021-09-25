from django import template

register = template.Library()


# TODO: make dynamic modal
@register.filter(name='lookup')
def lookup(value, arg):
    return value.get(pk=arg).name
