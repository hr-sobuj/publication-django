from django import template
import re

register = template.Library()
@register.filter()
def discount_price(price,discount):
    try:
        return (int(price-((price)*discount/100)))
    except (ValueError, ZeroDivisionError):
        return ""

