#!/usr/bin/env python3
import re
from . import Speller, Tokenizer, KnownWords


def is_english(word):
    return all('a' <= w <= 'z' for w in word)


def not_in_known_words(word):
    return word not in KnownWords


def sanitize_message(message):
    untagged = re.sub(r'<[0-9a-z_/]+>', '', message)
    return re.sub(r'%[0-9lz\.\s$]*[scfd]', '', untagged)


def spell_check(message):
    words = filter(is_english, Tokenizer.findall(sanitize_message(message)))
    unknowns = filter(not_in_known_words, Speller.unknown(words))
    return list(unknowns)
