import string
text=input("Введіть рядок:")
words = text.split()
hashtag = '#' + ''.join(word.capitalize() for word in words)
hashtag = ''.join(ch for ch in hashtag if ch not in string.punctuation and not ch.isspace())
if len(hashtag) > 140:
    hashtag = hashtag[:140]
print("Ваш хештег:", hashtag)