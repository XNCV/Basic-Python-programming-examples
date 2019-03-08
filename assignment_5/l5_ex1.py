def abc_range(start, end):
    num_start = ord(start)
    num_end = ord(end)
    # Incremental
    if num_start < num_end:
        for i in range(num_start, num_end):
            yield chr(i)
    # Decremental
    else:
        for i in range(num_start, num_end, -1):
            yield chr(i)


generator_abc = abc_range('d', 'a')
print(next(generator_abc))
print(next(generator_abc))
print(next(generator_abc))
print(next(generator_abc))
print(next(generator_abc))
