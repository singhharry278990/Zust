from django import template
from videography_app.models import *
from django.db.models import Max
from django.db.models import F, Value, CharField
from django.db.models.functions import Concat


register = template.Library()

@register.filter(is_safe=True)
def custom_image_tag(image_data, args):

    class_name = None
    data = args.split("-")
   
    image_data = []
    if data:
        class_name = data[0].split("=")
        image_id = data[1].split("=")
        class_name = class_name[1]
        image_id = image_id[1]
    else:
        return None