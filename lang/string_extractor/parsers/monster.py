from ..helper import get_singular_name
from ..write_text import write_text


def parse_monster_concrete(json, origin, name):
    if "description" in json:
        write_text(
            json["description"],
            origin,
            c_format=False,
            comment=f'Description of monster \"{name}\"',
        )

    if "death_function" in json:
        if "message" in json["death_function"]:
            write_text(
                json["death_function"]["message"],
                origin,
                comment=f'Death message of monster \"{name}\"',
            )

    if "special_attacks" in json:
        for attack in json["special_attacks"]:
            if "description" in attack:
                write_text(
                    attack["description"],
                    origin,
                    comment=f'Description of special attack of monster \"{name}\"',
                )
            if "monster_message" in attack:
                write_text(
                    attack["monster_message"],
                    origin,
                    comment=f'Monster message of special attack of monster \"{name}\"',
                )
            if "targeting_sound" in attack:
                write_text(
                    attack["targeting_sound"],
                    origin,
                    comment=f'Targeting sound of special attack of monster \"{name}\"',
                )
            if "no_ammo_sound" in attack:
                write_text(
                    attack["no_ammo_sound"],
                    origin,
                    comment=f'No ammo sound of special attack of monster \"{name}\"',
                )


def parse_monster(json, origin):
    name = ""
    if "name" in json:
        name = get_singular_name(json["name"])
        write_text(json["name"], origin, comment="Monster name", plural=True)
    elif "id" in json:
        name = json["id"]

    parse_monster_concrete(json, origin, name)

    if "extend" in json:
        parse_monster_concrete(json["extend"], origin, name)
