def get_substring_positions(str1, str2):
    def get_substrings(s):
        return [s[i:i+2] for i in range(len(s) - 1)]
    
    substrings1 = set(get_substrings(str1))
    substrings2 = set(get_substrings(str2))
    common_substrings = substrings1.intersection(substrings2)
    return len(common_substrings)

# Contoh penggunaan:
print(get_substring_positions("dobatz", "docatzz"))  # Output: 3
