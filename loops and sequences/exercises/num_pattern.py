def number_pattern(n):

    numbers = []

    if n < 1:
        return print('Argument must be an integer greater than 0.')

    if not isinstance(n, int):
        return print('Argument must be an integer value.')

    for num in range(1, n+1):
        numbers.append(str(num))

    return ' '.join(numbers)

print(number_pattern(12))