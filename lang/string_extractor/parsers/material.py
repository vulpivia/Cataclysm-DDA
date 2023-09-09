from ..helper import get_singular_name
from ..write_text import write_text


def parse_material(json, origin):
    name = get_singular_name(json["name"])
    write_text(name, origin, comment="Name of material")

    if "bash_dmg_verb" in json:
        write_text(
            json["bash_dmg_verb"],
            origin,
            comment=f"Bash damage verb of material {name}",
        )

    if "cut_dmg_verb" in json:
        write_text(
            json["cut_dmg_verb"],
            origin,
            comment=f"Cut damage verb of material {name}",
        )

    if "dmg_adj" in json:
        for i in range(4):
            write_text(
                json["dmg_adj"][i],
                origin,
                comment=f"Damage adjective of material {name}",
            )
