PREFIXES = ["ال","وال","بال","كال","فال","لل"]
SUFFIXES = ["ه","ها","هم","كم","نا","ات","ون","ين","ة"]

def light_stem(word: str) -> str:
    for p in PREFIXES:
        if word.startswith(p) and len(word) > len(p) + 2:
            word = word[len(p):]
    for s in SUFFIXES:
        if word.endswith(s) and len(word) > len(s) + 2:
            word = word[:-len(s)]
    return word
