from ..helper import get_singular_name
from ..write_text import write_text


def parse_gunmod(json, origin):
    write_text(json["name"], origin, comment="Gun mod name", plural=True)
    name = get_singular_name(json["name"])

    if "description" in json:
        write_text(
            json["description"],
            origin,
            comment=f'Description of gun mod \"{name}\"',
        )

    if "mode_modifier" in json:
        for mode in json["mode_modifier"]:
            write_text(mode[1], origin, comment=f'Firing mode of gun mod \"{name}\"')

    if "location" in json:
        write_text(json["location"], origin, comment=f'Location of gun mod \"{name}\"')

    if "mod_targets" in json:
        for target in json["mod_targets"]:
            write_text(
                target,
                origin,
                context="gun_type_type",
                comment=f'Target of gun mod \"{name}\"',
            )
