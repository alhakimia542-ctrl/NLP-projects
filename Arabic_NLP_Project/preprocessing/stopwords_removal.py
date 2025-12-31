ARABIC_STOPWORDS = {
    "في","على","من","الى","عن","ما","هذا","هذه","هو","هي","ذلك","كان","و","ب","ل"
}

def remove_stopwords(tokens):
    return [w for w in tokens if w not in ARABIC_STOPWORDS]
