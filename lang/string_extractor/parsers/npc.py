from ..write_text import write_text


def parse_npc(json, origin):
    gender = f'a {json["gender"]}' if "gender" in json else "an"
    comment = json.get("//", None)
    if "name_unique" in json:
        write_text(
            json["name_unique"],
            origin,
            comment=[f"Unique name of {gender} NPC", comment],
        )
    if "name_suffix" in json:
        write_text(
            json["name_suffix"],
            origin,
            comment=[f"Name suffix of {gender} NPC", comment],
        )
