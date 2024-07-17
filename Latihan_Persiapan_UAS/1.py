def sortAndDisplay(data):
    # Loop over the valid indices of the list in increasing order
    for i in range(len(data)):
        # Loop over the valid indices of the list in decreasing order
        for j in range((len(data)-1), 0, -1): # --(bug 1: Akan terjadi out of range error pada list jika dimulai dari panjang data tanpa dikurangi 1)-- 
            # If two adjacent elements are out of order
            if data[j] < data[j-1]:
                # Swap the element at pos. j with the element at pos. j-1
                t = data[j]
                data[j] = data[j-1]
                data[j-1] = t # --(bug 2: data[j-1] seharusnya menyimpan value dari t)--
    # Display the result on the screen
    return(data) # --(bug 3: Indentation error)--

# Contoh penggunaan:
print(f"After sort {sortAndDisplay([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])}")