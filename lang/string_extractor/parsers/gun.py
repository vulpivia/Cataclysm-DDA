from ..helper import get_singular_name
from ..write_text import write_text


def parse_gun(json, origin):
    name = ""
    if "name" in json:
        name = get_singular_name(json["name"])
        write_text(json["name"], origin, comment="Name of a gun", plural=True)
    elif "id" in json:
        name = json["id"]

    if "description" in json:
        write_text(
            json["description"],
            origin,
            comment=f'Description of gun \"{name}\"',
        )

    if "variants" in json:
        for variant in json["variants"]:
            variant_name = get_singular_name(variant["name"])
            write_text(
                variant["name"],
                origin,
                comment=f'Variant name of gun \"{name}\"',
                plural=True,
            )
            write_text(variant["description"], origin,
                       comment="Description of variant \"{0}\" of gun \"{1}\""
                       .format(name, variant_name))

    if "modes" in json:
        for mode in json["modes"]:
            write_text(mode[1], origin, comment=f'Firing mode of gun \"{name}\"')

    if "skill" in json:
        if json["skill"] != "archery":
            write_text(
                json["skill"],
                origin,
                context="gun_type_type",
                comment=f'Skill associated with gun \"{name}\"',
            )

    if "reload_noise" in json:
        write_text(
            json["reload_noise"],
            origin,
            comment=f'Reload noise of gun \"{name}\"',
        )

    if "valid_mod_locations" in json:
        for loc in json["valid_mod_locations"]:
            write_text(loc[0], origin, comment=f'Valid mod location of gun \"{name}\"')
