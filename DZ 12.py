import string
s = input()
start, end = s.split("-")
letters = string.ascii_letters
start_index = letters.index(start)
end_index = letters.index(end)
print(letters[start_index:end_index+1])