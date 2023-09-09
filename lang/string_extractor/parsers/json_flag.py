from ..write_text import write_text


def parse_json_flag(json, origin):
    if "info" in json:
        write_text(
            json["info"],
            origin,
            c_format=False,
            comment=[
                "Please leave anything in <angle brackets> unchanged.",
                f'Description of JSON flag \"{json["id"]}\"',
            ],
        )
    if "restriction" in json:
        write_text(
            json["restriction"],
            origin,
            c_format=False,
            comment=f'Description of restriction of JSON flag \"{json["id"]}\"',
        )
