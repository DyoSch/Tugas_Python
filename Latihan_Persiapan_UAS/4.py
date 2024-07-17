def sum_without_twenties(a, b, c):
    def filter_twenty(x):
        return x if x < 20 or x > 29 else 0
    
    return filter_twenty(a) + filter_twenty(b) + filter_twenty(c)

# Contoh penggunaan:
print(sum_without_twenties(5, 21, 32))  # Output: 37
print(sum_without_twenties(20, 25, 29))  # Output: 0