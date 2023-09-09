#!/usr/bin/env python3
import polib
import os
import re
import sys


tags = set()
ignore_tags = {'<1>', '<2>', '<3>', '<4>', '<f>', '<n>',
               '<q>', '<r>', '<s>', '<u>', '<more>', '<empty>'}
pattern = re.compile(r'<[a-z/0-9_]+>')


def init_tags():
    global tags
    pofile = polib.pofile("./lang/po/cataclysm-dda.pot")
    for entry in pofile:
        for tag in set(pattern.findall(entry.msgid)):
            tags.add(tag)
    tags = tags - ignore_tags


def extract_tags(msg):
    matches = pattern.findall(msg)
    return {match for match in matches if match in tags}


def check_message(entry):
    msgid = entry.msgid
    msgstr = entry.msgstr
    if not msgstr:
        return set()
    tags_msgid = extract_tags(msgid)
    tags_msgstr = extract_tags(msgstr)
    return tags_msgid - tags_msgstr


def check_po_file(file):
    pofile = polib.pofile(file)
    errors = 0
    for entry in pofile.translated_entries():
        if missing_tags := check_message(entry):
            print("Tag(s) {} missing in translation: {} => {}".format(
                missing_tags,
                entry.msgid.replace("\n", "\\n"),
                entry.msgstr.replace("\n", "\\n")))
            errors += 1
    return errors


init_tags()
po_files = [
    file
    for file in sorted(os.listdir("lang/po"))
    if file.endswith(".po") and not file.endswith("en.po")
]
files_to_check = []
if len(sys.argv) == 1:
    files_to_check = po_files
else:
    for i in range(1, len(sys.argv)):
        if f"{sys.argv[i]}.po" in po_files:
            files_to_check.append(f"{sys.argv[i]}.po")
        else:
            print("Warning: Unknown language", sys.argv[i])
num_errors = 0
for file in sorted(files_to_check):
    print(f"Checking {file}")
    num_errors += check_po_file(f"lang/po/{file}")
    print()
exit(num_errors)
