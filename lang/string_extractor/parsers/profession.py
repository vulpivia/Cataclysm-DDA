from ..write_text import write_text


def parse_profession(json, origin):
    name_male = ""
    name_female = ""
    if "name" not in json:
        name_male = name_female = json["id"]
    elif type(json["name"]) is dict:
        name_male = json["name"]["male"]
        name_female = json["name"]["female"]
    elif type(json["name"]) is str:
        name_male = name_female = json["name"]

    write_text(name_male, origin, context="profession_male",
               comment="Profession name for male")
    write_text(
        json["description"],
        origin,
        context="prof_desc_male",
        comment=f'Description of profession \"{name_male}\" for male',
    )

    write_text(name_female, origin, context="profession_female",
               comment="Profession name for female")
    write_text(
        json["description"],
        origin,
        context="prof_desc_female",
        comment=f'Description of profession \"{name_female}\" for female',
    )
