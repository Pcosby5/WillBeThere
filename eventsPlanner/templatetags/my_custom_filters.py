from django import template

register = template.Library()

@register.filter(name='join_list')
def join_list(value, arg):
    return arg.join(value)
