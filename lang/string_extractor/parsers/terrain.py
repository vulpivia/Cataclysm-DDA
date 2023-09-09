from ..helper import get_singular_name
from ..write_text import write_text


def parse_terrain(json, origin):
    name = get_singular_name(json.get("name", json["id"]))
    if "name" in json:
        write_text(json["name"], origin, comment="Terrain name")
    if "description" in json:
        write_text(
            json["description"],
            origin,
            comment=f'Description of terrain \"{name}\"',
        )
    if "bash" in json:
        if "sound" in json["bash"]:
            write_text(
                json["bash"]["sound"],
                origin,
                comment=f'Bashing sound of terrain \"{name}\"',
            )
        if "sound_fail" in json["bash"]:
            write_text(
                json["bash"]["sound_fail"],
                origin,
                comment=f'Bashing failed sound of terrain \"{name}\"',
            )
    if "boltcut" in json:
        if "message" in json["boltcut"]:
            write_text(
                json["boltcut"]["message"],
                origin,
                comment=f'Boltcut message of terrain \"{name}\"',
            )
        if "sound" in json["boltcut"]:
            write_text(
                json["boltcut"]["sound"],
                origin,
                comment=f'Boltcut sound of terrain \"{name}\"',
            )
    if "hacksaw" in json:
        if "message" in json["hacksaw"]:
            write_text(
                json["hacksaw"]["message"],
                origin,
                comment=f'Hacksaw message of terrain \"{name}\"',
            )
        if "sound" in json["hacksaw"]:
            write_text(
                json["hacksaw"]["sound"],
                origin,
                comment=f'Hacksaw sound of terrain \"{name}\"',
            )
