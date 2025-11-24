def generate_cube_numbers(end):
    num = 2
    while True:
        cube = num**3
        if cube > end:
            return
        yield cube
        num += 1


from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True
assert list(generate_cube_numbers(10))
assert list(generate_cube_numbers(100))
assert list(generate_cube_numbers(1000))
print("OK")
