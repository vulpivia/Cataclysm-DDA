from ..helper import get_singular_name
from ..write_text import write_text


def parse_technique(json, origin):
    name = ""
    if "name" in json:
        name = get_singular_name(json["name"])
        write_text(json["name"], origin, comment="Martial technique name")

    if "description" in json:
        write_text(
            json["description"],
            origin,
            c_format=False,
            comment=f'Description of martial technique \"{name}\"',
        )

    for msg in json.get("messages", []):
        write_text(msg, origin, comment=f'Message of martial technique \"{name}\"')
