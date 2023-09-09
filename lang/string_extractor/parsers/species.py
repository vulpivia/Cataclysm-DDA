from ..write_text import write_text


def parse_species(json, origin):
    id = json["id"]
    if "description" in json:
        write_text(
            json["description"],
            origin,
            comment=f'Description of species \"{id}\"',
        )
    if "footsteps" in json:
        write_text(
            json["footsteps"],
            origin,
            comment=f'Foot steps of species \"{id}\"',
        )
