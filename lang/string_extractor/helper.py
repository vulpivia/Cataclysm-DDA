import re


def get_singular_name(name):
    if type(name) is dict and "str_sp" in name:
        return name["str_sp"]
    elif type(name) is dict and "str" in name:
        return name["str"]
    elif type(name) is dict or type(name) is not str:
        raise Exception(f"Cannot find singular name in {name}")
    else:
        return name


tag_pattern = re.compile(r'^<[a-z0-9_]*>$')


def is_tag(text):
    return tag_pattern.match(text)
