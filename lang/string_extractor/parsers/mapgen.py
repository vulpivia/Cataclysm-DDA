from ..helper import get_singular_name
from ..write_text import write_text


def parse_mapgen(json, origin):
    if "object" not in json:
        return

    om = ""
    if "om_terrain" in json:
        if type(json["om_terrain"]) is str:
            om = json["om_terrain"]
        elif type(json["om_terrain"]) is list:
            if len(json["om_terrain"]) == 0:
                om = ""
            elif type(json["om_terrain"][0]) is str:
                om = ", ".join(json["om_terrain"])
            elif type(json["om_terrain"][0]) is list:
                om = ", ".join(", ".join(i) for i in json["om_terrain"])

    for key in ["place_specials", "place_signs"]:
        if key in json["object"]:
            for sign in json["object"][key]:
                if "signage" in sign:
                    write_text(sign["signage"], origin, comment=f"Signage placed on map {om}")

    if "signs" in json["object"]:
        for sign in json["object"]["signs"]:
            if "signage" in json["object"]["signs"][sign]:
                write_text(
                    json["object"]["signs"][sign]["signage"],
                    origin,
                    comment=f"Signage placed on map {om}",
                )

    if "computers" in json["object"]:
        for key in json["object"]["computers"]:
            com = json["object"]["computers"][key]
            com_name = ""
            if "name" in com:
                com_name = get_singular_name(com["name"])
                write_text(com["name"], origin, comment=f"Computer name placed on map {om}")
            for opt in com.get("options", []):
                if "name" in opt:
                    write_text(
                        opt["name"],
                        origin,
                        comment=f'Interactive menu name in computer \"{com_name}\" placed on map {om}',
                    )
            if "access_denied" in com:
                write_text(
                    com["access_denied"],
                    origin,
                    comment=f'Access denied message on computer \"{com_name}\" placed on map {om}',
                )
