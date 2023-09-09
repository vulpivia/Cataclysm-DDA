from ..write_text import write_text


def parse_event_statistic(json, origin):
    if "description" in json:
        write_text(
            json["description"],
            origin,
            comment=f'Description of event statistic \"{json["id"]}\"',
            plural=True,
        )
