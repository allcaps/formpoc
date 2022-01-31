import json

from django import template
from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def jsonify(obj):
    if isinstance(obj, QuerySet):  # type: ignore # https://github.com/typeddjango/django-stubs/issues/704
        return mark_safe(serialize("json", obj))
    return mark_safe(json.dumps(obj))
