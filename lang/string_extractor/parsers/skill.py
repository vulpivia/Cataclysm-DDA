from ..helper import get_singular_name
from ..write_text import write_text


def parse_skill(json, origin):
    name = ""
    if "name" in json:
        name = get_singular_name(json["name"])
        write_text(json["name"], origin, comment="Skill name")

    if "description" in json:
        write_text(
            json["description"],
            origin,
            comment=f'Description of skill \"{name}\"',
        )
