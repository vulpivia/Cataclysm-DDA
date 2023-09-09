from ..helper import get_singular_name
from ..write_text import write_text


def parse_furniture(json, origin):
    name = get_singular_name(json.get("name", json["id"]))
    if "name" in json:
        write_text(json["name"], origin, comment="Furniture name")
    if "description" in json:
        write_text(
            json["description"],
            origin,
            comment=f'Description of furniture \"{name}\"',
        )
    if "bash" in json:
        if "sound" in json["bash"]:
            write_text(
                json["bash"]["sound"],
                origin,
                comment=f'Bashing sound of furniture \"{name}\"',
            )
        if "sound_fail" in json["bash"]:
            write_text(
                json["bash"]["sound_fail"],
                origin,
                comment=f'Bashing failed sound of furniture \"{name}\"',
            )
