def count_occurrences(char, string):
    count = 0
    for i in string:
        if i == char:
            count += 1
    return count

# Contoh penggunaan:
print(count_occurrences('o', 'Hello World!'))  # Output: 2
print(count_occurrences('z', 'Hello World!'))  # Output: 0