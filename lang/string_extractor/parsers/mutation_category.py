from ..helper import get_singular_name
from ..write_text import write_text


def parse_mutation_category(json, origin):
    name = get_singular_name(json["name"])
    write_text(json["name"], origin, comment="Mutation class name")

    for key in ["mutagen_message",
                "iv_message",
                "iv_sleep_message",
                "iv_sound_message",
                "junkie_message"
                ]:
        if key in json:
            write_text(
                json[key],
                origin,
                comment=f'\"{key}\" of mutation class \"{name}\"',
            )

    if "memorial_message" in json:
        write_text(
            json["memorial_message"],
            origin,
            context="memorial_male",
            comment=f'Memorial message of mutation class \"{name}\" for male',
        )
        write_text(
            json["memorial_message"],
            origin,
            context="memorial_female",
            comment=f'Memorial message of mutation class \"{name}\" for female',
        )
