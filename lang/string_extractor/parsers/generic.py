from ..helper import get_singular_name
from .use_action import parse_use_action
from ..write_text import write_text


def parse_generic(json, origin):
    name = ""
    comment = []
    if "//" in json:
        comment.append(json["//"])
    if "//isbn13" in json:
        comment.append(f'ISBN {json["//isbn13"]}')

    if "name" in json:
        name = get_singular_name(json["name"])
        write_text(json["name"], origin, comment=comment + ["Item name"],
                   plural=True, c_format=False)
    elif "id" in json:
        name = json["id"]

    if "description" in json:
        write_text(
            json["description"],
            origin,
            c_format=False,
            comment=comment + [f'Description of \"{name}\"'],
        )

    if "use_action" in json:
        parse_use_action(json["use_action"], origin, name)

    for cname in json.get("conditional_names", []):
        write_text(
            cname["name"],
            origin,
            comment=f'Conditional name for \"{name}\" when {cname["type"]} matches {cname["condition"]}',
            plural=True,
        )

    if "snippet_category" in json and type(json["snippet_category"]) is list:
        # snippet_category is either a simple string (the category ident)
        # which is not translated, or an array of snippet texts.
        for entry in json["snippet_category"]:
            if type(entry) is str:
                write_text(entry, origin, comment=f'Snippet of item \"{name}\"')
            elif type(entry) is dict:
                write_text(entry["text"], origin, comment=f'Snippet of item \"{name}\"')

    if "seed_data" in json:
        write_text(
            json["seed_data"]["plant_name"],
            origin,
            comment=f'Plant name of seed \"{name}\"',
        )

    if "revert_msg" in json:
        write_text(
            json["revert_msg"],
            origin,
            comment=f'Dying message of tool \"{name}\"',
        )

    if "pocket_data" in json:
        for pocket in json["pocket_data"]:
            if "description" in pocket:
                write_text(
                    pocket["description"],
                    origin,
                    comment=f'Description of a pocket in item \"{name}\"',
                )
            if "name" in pocket:
                write_text(
                    pocket["name"],
                    origin,
                    comment=f'Brief name of a pocket in item \"{name}\"',
                )
