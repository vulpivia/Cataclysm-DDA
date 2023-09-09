from ..write_text import write_text


def parse_item_action(json, origin):
    if "name" in json:
        write_text(
            json["name"],
            origin,
            comment=f'Item action name of \"{json["id"]}\"',
        )
