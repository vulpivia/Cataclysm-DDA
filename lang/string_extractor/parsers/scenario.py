from ..write_text import write_text


def parse_scenario(json, origin):
    name = ""
    if "name" in json:
        name = json["name"]
        write_text(name, origin, context="scenario_male",
                   comment="Scenario name for male")
        write_text(name, origin, context="scenario_female",
                   comment="Scenario name for female")
    if name == "":
        name = json["id"]

    if "description" in json:
        write_text(
            json["description"],
            origin,
            context="scen_desc_male",
            comment=f'Description of scenario \"{name}\" for male',
        )
        write_text(
            json["description"],
            origin,
            context="scen_desc_female",
            comment=f'Description of scenario \"{name}\" for female',
        )

    if "start_name" in json:
        write_text(
            json["start_name"],
            origin,
            context="start_name",
            comment=f'Starting location of scenario \"{name}\"',
        )
