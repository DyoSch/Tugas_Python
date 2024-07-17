def count_unique_words(path_file):
    line_counts = {}
    with open(path_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line in line_counts:
                line_counts[line] += 1
            else:
                line_counts[line] = 1
    
    if len(line_counts) == 0:
        print("File is empty.")
    else:
        for line, count in line_counts.items():
            print(f"{count}    {line}")

# Contoh penggunaan:
count_unique_words('input_sample.txt')
