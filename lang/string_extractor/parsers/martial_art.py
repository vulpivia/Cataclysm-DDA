from ..helper import get_singular_name
from ..write_text import write_text


def parse_martial_art(json, origin):
    name = get_singular_name(json["name"])
    write_text(name, origin, comment="Name of martial art")

    if "description" in json:
        write_text(
            json["description"],
            origin,
            c_format=False,
            comment=f'Description of martial art \"{name}\"',
        )

    if "initiate" in json:
        messages = json["initiate"]
        if type(messages) is str:
            messages = [messages]
        for msg in messages:
            write_text(msg, origin, comment=f'Initiate message of martial art \"{name}\"')

    onhit_buffs = json.get("onhit_buffs", [])
    static_buffs = json.get("static_buffs", [])
    onmove_buffs = json.get("onmove_buffs", [])
    ondodge_buffs = json.get("ondodge_buffs", [])
    onattack_buffs = json.get("onattack_buffs", [])
    onpause_buffs = json.get("onpause_buffs", [])
    onblock_buffs = json.get("onblock_buffs", [])
    ongethit_buffs = json.get("ongethit_buffs", [])
    onmiss_buffs = json.get("onmiss_buffs", [])
    oncrit_buffs = json.get("oncrit_buffs", [])
    onkill_buffs = json.get("onkill_buffs", [])

    buffs = (onhit_buffs + static_buffs + onmove_buffs + ondodge_buffs +
             onattack_buffs + onpause_buffs + onblock_buffs + ongethit_buffs +
             onmiss_buffs + oncrit_buffs + onkill_buffs)

    for buff in buffs:
        buff_name = get_singular_name(buff["name"])
        write_text(buff_name, origin, comment=f'Buff name of martial art \"{name}\"')
        write_text(buff["description"], origin, c_format=False,
                   comment="Description of buff \"{0}\" in martial art "
                           "\"{1}\"".format(name, buff_name))
