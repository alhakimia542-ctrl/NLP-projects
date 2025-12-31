from preprocessing.normalization import normalize_arabic
from preprocessing.tokenization import tokenize
from preprocessing.stopwords_removal import remove_stopwords
from stemming.light_stemmer import light_stem
from stemming.khoja_stemmer import khoja_stem

text = "الطلاب يدرسون معالجة اللغات الطبيعية في الجامعة"

normalized = normalize_arabic(text)
tokens = tokenize(normalized)
tokens = remove_stopwords(tokens)

print("Tokens:", tokens)
print("Light Stemmer:", [light_stem(w) for w in tokens])
print("Khoja Stemmer:", [khoja_stem(w) for w in tokens])
