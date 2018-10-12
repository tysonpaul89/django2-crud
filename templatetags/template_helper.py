"""
Custom template tag
"""
from django.template.defaulttags import register

@register.filter
def get_dict_item(dictionary, key):
    """
    Tag to get item from a dictionary
    Ref:
    https://stackoverflow.com/questions/8000022/django-template-how-to-look-up-a-dictionary-value-with-a-variable/8000091#8000091
    https://stackoverflow.com/questions/6451304/django-simple-custom-template-tag-example/6493001#6493001
    """
    return dictionary.get(key)
