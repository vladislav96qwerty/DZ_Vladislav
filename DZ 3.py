list = [45, 8, 1, 55]
if len(list) > 1:
    last_element = list.pop()
    list.insert(0, last_element)
print(list)