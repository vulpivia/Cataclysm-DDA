from ..write_text import write_text


def parse_start_location(json, origin):
    write_text(
        json["name"],
        origin,
        comment=f'Name of starting location \"{json["id"]}\"',
    )
