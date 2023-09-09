#!/usr/bin/env python3
from spell_checker.spell_checker import spell_check
import polib


pofile = polib.pofile('./lang/po/cataclysm-dda.pot')
# occurrences = dict()
for entry in pofile:
    if typos := spell_check(entry.msgid):
        print(typos, "<=", entry.msgid.replace('\n', '\\n'))
