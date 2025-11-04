import keyword
import string
s = input("Введіть рядок: ")
if not s:
    print(False)
elif s in keyword.kwlist:
    print(False)
elif s[0].isdigit():
    print(False)
elif " " in s:
    print(False)
elif any(ch.isupper() for ch in s):
    print(False)
elif any(ch in string.punctuation.replace("_", "") for ch in s):
    print(False)
elif s.count("_") == len(s) and len(s) > 1:
    print(False)
else:
    print(True)
