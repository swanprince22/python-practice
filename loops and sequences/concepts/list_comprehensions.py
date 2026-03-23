even_numbers = []

for num in range(21):
    if num%2 == 0:
        even_numbers.append(num)

print(even_numbers)

even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)

numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words  = list(filter(is_long_word, words))
print(long_words)

