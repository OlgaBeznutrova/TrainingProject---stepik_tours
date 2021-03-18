from typing import Union

from django import template

register = template.Library()


@register.filter
def human_readable_price(value):
    return f'{value:,}'.replace(',', ' ')


@register.filter
def stars(value):
    return "★" * int(value)


@register.filter
def ru_pluralize(number: Union[int, str], arg: str = "тур,тура,туров"):
    nominative_singular, genitive_singular, genitive_plural = arg.split(",")
    number = abs(int(number))

    if 10 <= number % 100 <= 20:
        return f"{number} {genitive_plural}"
    if number % 10 == 1:
        return f"{number} {nominative_singular}"
    if 2 <= number % 10 <= 4:
        return f"{number} {genitive_singular}"
    return f"{number} {genitive_plural}"
