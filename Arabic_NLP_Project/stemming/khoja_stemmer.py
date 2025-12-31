import re

PATTERNS = [
    r'^م(.{3})$',
    r'^(.{3})ات$',
    r'^ال(.{3})$'
]

def khoja_stem(word: str) -> str:
    for p in PATTERNS:
        m = re.match(p, word)
        if m:
            return m.group(1)
    return word
