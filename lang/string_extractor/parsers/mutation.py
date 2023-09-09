from ..helper import get_singular_name
from ..write_text import write_text


def parse_mutation(json, origin):
    name = ""
    if "name" in json:
        name = get_singular_name(json["name"])
        write_text(json["name"], origin, comment="Mutation name")

    if "description" in json:
        write_text(
            json["description"],
            origin,
            c_format=False,
            comment=f'Description of mutation \"{name}\"',
        )

    if "attacks" in json:
        attacks = json["attacks"]
        if type(attacks) is dict:
            attacks = [attacks]
        for attack in attacks:
            if "attack_text_u" in attack:
                write_text(
                    attack["attack_text_u"],
                    origin,
                    comment=f'Message when player with mutation \"{name}\" attacks',
                )
            if "attack_text_npc" in attack:
                write_text(
                    attack["attack_text_npc"],
                    origin,
                    comment=f'Message when NPC with mutation \"{name}\" attacks',
                )

    if "ranged_mutation" in json:
        if "message" in json["ranged_mutation"]:
            write_text(
                json["ranged_mutation"]["message"],
                origin,
                comment=f'Message when firing ranged attack with mutation \"{name}\"',
            )

    if "spawn_item" in json:
        if "message" in json["spawn_item"]:
            write_text(
                json["spawn_item"]["message"],
                origin,
                comment=f'Message when spawning item \"{json["spawn_item"]["type"]}\" with mutation \"{name}\"',
            )

    if "triggers" in json:
        for arr in json["triggers"]:
            for trigger in arr:
                if "msg_on" in trigger and "text" in trigger["msg_on"]:
                    write_text(
                        trigger["msg_on"]["text"],
                        origin,
                        comment=f'Trigger message of mutation \"{name}\"',
                    )
                if "msg_off" in trigger and "text" in trigger["msg_off"]:
                    write_text(
                        trigger["msg_off"]["text"],
                        origin,
                        comment=f'Trigger message of mutation \"{name}\"',
                    )

    if "transform" in json:
        write_text(
            json["transform"]["msg_transform"],
            origin,
            comment=f'Message when transforming from mutation  \"{name}\" to \"{json["transform"]["target"]}\"',
        )
