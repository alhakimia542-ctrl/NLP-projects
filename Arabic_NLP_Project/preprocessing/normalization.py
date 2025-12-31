import re

def normalize_arabic(text: str) -> str:
    text = re.sub(r'[ًٌٍَُِّْـ]', '', text)
    text = re.sub('[إأآا]', 'ا', text)
    text = re.sub('ى', 'ي', text)
    text = re.sub('ؤ', 'و', text)
    text = re.sub('ئ', 'ي', text)
    text = re.sub('ة', 'ه', text)
    text = re.sub(r'[^\u0600-\u06FF\s]', '', text)
    return text
