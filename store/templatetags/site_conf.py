from django import template
from django.conf import settings

register = template.Library()

# website global settings
@register.simple_tag
def PRIMARY_COLOR():
    return "violet"