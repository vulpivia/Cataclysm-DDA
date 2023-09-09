from ..write_text import write_text


def parse_dream(json, origin):
    for msg in json.get("messages", []):
        write_text(
            msg,
            origin,
            comment=f'Dream of mutation category \"{json["category"]}\"',
        )
