from ..write_text import write_text


def parse_weakpoint_set(json, origin):
    if "weakpoints" not in json:
        return
    for wp in json["weakpoints"]:
        id = ""
        if "id" in wp:
            id = wp["id"]
        if "name" in wp:
            comment = f'Sentence fragment describing the \"{id}\" weakpoint'
            write_text(wp["name"], origin, comment=comment)
        if "effects" in wp:
            for fx in wp["effects"]:
                if "message" in fx:
                    comment = f'Message describing the effect of hitting the \"{id}\" weakpoint'
                    write_text(fx["message"], origin, comment=comment)
