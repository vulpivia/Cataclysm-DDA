from ..helper import get_singular_name
from ..write_text import write_text


def parse_movement_mode(json, origin):
    name = get_singular_name(json["name"])
    write_text(json["name"], origin, comment="Movement mode name")
    write_text(
        json["character"],
        origin,
        comment=f'Character displayed in the move menu for movement mode \"{name}\"',
    )
    write_text(
        json["panel_char"],
        origin,
        comment=f'Character displayed in the panel for movement mode \"{name}\"',
    )
    write_text(
        json["change_good_none"],
        origin,
        comment=f'Successfully switched to movement mode \"{name}\" with no steed',
    )
    write_text(
        json["change_good_animal"],
        origin,
        comment=f'Successfully switched to movement mode \"{name}\" with animal steed',
    )
    write_text(
        json["change_good_mech"],
        origin,
        comment=f'Successfully switched to movement mode \"{name}\" with mechanical steed',
    )
    if "change_bad_none" in json:
        write_text(
            json["change_bad_none"],
            origin,
            comment=f'Failed to switched to movement mode \"{name}\" with no steed',
        )
    if "change_bad_animal" in json:
        write_text(
            json["change_bad_animal"],
            origin,
            comment=f'Failed to switched to movement mode \"{name}\" with animal steed',
        )
    if "change_bad_mech" in json:
        write_text(
            json["change_bad_mech"],
            origin,
            comment=f'Failed to switched to movement mode \"{name}\" with mechanical steed',
        )
