from .message import Message, messages, occurrences


def append_comment(comments, new_comment):
    if type(new_comment) is str:
        return comments + new_comment.split("\n")
    elif type(new_comment) is list:
        for comment in new_comment:
            if comment:
                comments = append_comment(comments, comment)
        return comments


def write_text(json, origin, context="", comment="",
               plural=False, c_format=True):
    """
    Record a text for translation.

    Parameters:
        json: The text in string or JSON dict form
        origin (str): Path of JSON source location
        context (str): "context" as in GNU gettext
        comment: Translation comments in either string form or list of strings
        plural (bool): Whether the text should be pluralized
        c_format (bool): Whether the text contains C-style format string
    """
    if json is None or json == "":
        return

    comments = append_comment([], comment)
    text = ""
    text_plural = ""

    if type(json) is str:
        text = json
        if plural:
            text_plural = f"{text}s"
    elif type(json) is dict:
        if "//~" in json:
            if type(json["//~"]) is str and json["//~"]:
                comments = append_comment(comments, json["//~"])
        if "ctxt" in json:
            if type(json["ctxt"]) is str:
                context = json["ctxt"]
        if "str" in json:
            text = json["str"]
        if plural:
            if "str_sp" in json:
                text = json["str_sp"]
                text_plural = json["str_sp"]
            elif "str_pl" in json:
                text_plural = json["str_pl"]
            else:
                text_plural = f"{text}s"

    if not text:
        return

    format_tag = ""
    if "%" in text:
        format_tag = "c-format" if c_format else "no-c-format"
    if (context, text) not in messages:
        messages[(context, text)] = []

    messages[(context, text)].append(
        Message(comments, origin, format_tag, context, text, text_plural))
    occurrences.append((context, text))
