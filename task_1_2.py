odd_numbers_list = list(filter(lambda n: n % 2,[n for n in range(0, 1001)]))

odd_cubes_list = [n ** 3 for n in odd_numbers_list]

odd_cubes_division_list = list(filter(lambda n: not sum([int(d) for d in str(n)]) % 7,odd_cubes_list))

odd_cubes_division_plus_list = list(filter(lambda n: not sum([int(d) for d in str(n)]) % 7,[int(str(n) + "17") for n in odd_cubes_list]))

print(odd_cubes_division_plus_list)

