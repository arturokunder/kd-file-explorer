import re

from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()  # pylint: disable=C0103


@register.filter
@stringfilter
def formatfilename(value):
    if re.match(r'[ ]{0,1}[0-9a-fA-F]{24}', value) or re.match(r'[0-9a-fA-F]{24}\.(\w+)$', value):
      return value
    else:
      return re.sub(r'[ ]{0,1}[0-9a-fA-F]{24}', '', value.replace('-', ' '))

@register.filter
def checkValidObject(obj):
  if obj.is_subdir:
    return True
  elif obj.is_file and re.match(r'^.*\.(\w+)$', obj.basename):
    return True
  else:
    return False
