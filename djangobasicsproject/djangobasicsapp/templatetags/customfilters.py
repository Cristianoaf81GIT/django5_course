from django import template
from num2words import num2words

register = template.Library()


def first_five_upper(value: str) -> str:
    result = value[:5].upper()
    return result


def first_n_upper(value: str, n: int) -> str:
    result = value[:n].upper()
    return result


def length_limit(value: str, limit: int) -> str:
    if len(value) > limit:
        return value[0:limit] + "..."
    else:
        return value


def rating(value: str) -> str:
    if float(value) > 4:
        return f"{value} [Excelent]"
    elif float(value) >= 3:
        return f"{value} [Very good]"
    elif float(value) >= 1.5:
        return f"{value} [Average]"
    else:
        return f"{value} [Poor]"


def convert_num_2_word(value) -> str:
    return num2words(value)


register.filter("firstfiveupper", first_five_upper)
register.filter("firstnupper", first_n_upper)
register.filter("lengthlimit", length_limit)
register.filter("rating", rating)
register.filter("convertnumber2words", convert_num_2_word)
