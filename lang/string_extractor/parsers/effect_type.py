from ..write_text import write_text


def parse_effect_type(json, origin):
    effect_name = ""

    if "name" in json:
        names = set()
        for name in json["name"]:
            if type(name) is str:
                names.add(("", name))
            elif type(name) is dict:
                names.add((name["ctxt"], name["str"]))
        for (ctxt, name) in sorted(list(names), key=lambda x: x[1]):
            write_text(
                name,
                origin,
                context=ctxt,
                comment=f'Name of effect type id \"{json["id"]}\"',
            )
            effect_name = name if effect_name == "" else f"{effect_name}, {name}"
    if effect_name == "":
        effect_name = json["id"]

    if "desc" in json:
        descs = set()
        for desc in json["desc"]:
            if type(desc) is str:
                descs.add(("", desc))
            elif type(desc) is dict:
                descs.add((desc["ctxt"], desc["str"]))
        for (ctxt, desc) in sorted(list(descs), key=lambda x: x[1]):
            write_text(
                desc,
                origin,
                context=ctxt,
                comment=f'Description of effect type \"{effect_name}\"',
            )

    if "speed_name" in json:
        write_text(
            json["speed_name"],
            origin,
            comment=f'Speed name of effect type \"{effect_name}\"',
        )

    if "apply_message" in json:
        write_text(
            json["apply_message"],
            origin,
            comment=f'Apply message of effect type \"{effect_name}\"',
        )

    if "remove_message" in json:
        write_text(
            json["remove_message"],
            origin,
            comment=f'Remove message of effect type \"{effect_name}\"',
        )

    if "death_msg" in json:
        write_text(
            json["death_msg"],
            origin,
            comment=f'Death message of effect type \"{effect_name}\"',
        )

    if "miss_messages" in json:
        for msg in json["miss_messages"]:
            write_text(
                msg[0],
                origin,
                comment=f'Miss message of effect type \"{effect_name}\"',
            )

    if "decay_messages" in json:
        for msg in json["decay_messages"]:
            write_text(
                msg[0],
                origin,
                comment=f'Decay message of effect type \"{effect_name}\"',
            )

    if "apply_memorial_log" in json:
        write_text(
            json["apply_memorial_log"],
            origin,
            context="memorial_male",
            comment=f'Male memorial apply log of effect type \"{effect_name}\"',
        )
        write_text(
            json["apply_memorial_log"],
            origin,
            context="memorial_female",
            comment=f'Female memorial apply log of effect type \"{effect_name}\"',
        )

    if "remove_memorial_log" in json:
        write_text(
            json["remove_memorial_log"],
            origin,
            context="memorial_male",
            comment=f'Male memorial remove log of effect type \"{effect_name}\"',
        )
        write_text(
            json["remove_memorial_log"],
            origin,
            context="memorial_female",
            comment=f'Female memorial remove log of effect type \"{effect_name}\"',
        )
