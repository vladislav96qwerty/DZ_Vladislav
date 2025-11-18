def popular_words(text, words):
    text_lower = text.lower().split()
    result = {word: 0 for word in words}

    for word in text_lower:
        cleaned = word.strip(".,!?;:'\"()")
        if cleaned in result:
            result[cleaned] += 1

    return result
