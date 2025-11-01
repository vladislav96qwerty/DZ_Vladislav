def zeros(lst):
    zero_count = lst.count(0)
    while 0 in lst:
        lst.remove(0)
    for i in range(zero_count):
        lst.append(0)