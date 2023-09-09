from ..write_text import write_text


def parse_widget(json, origin):
    id = json["id"]
    if "label" in json:
        write_text(json["label"], origin, comment=f'Label of UI widget \"{id}\"')
    if "strings" in json:
        for string in json["strings"]:
            write_text(string, origin, comment=f'Text in UI widget \"{id}\"')
    if "phrases" in json:
        for phrase in json["phrases"]:
            comment = f'Text in portion of UI widget \"{id}\"'
            if "text" in phrase:
                write_text(phrase["text"], origin, comment=comment)
