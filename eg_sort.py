

"""
Like a hand of cards: maintains sorted left sub-array and repeatedly inserts into it
O(n^2), in-place, stable
"""
def insertion_sort(l: list) -> list:
    for i in range(1, len(l)):
        # Repeatedly shift elements rightward
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] > key:
            l[j + 1] = l[j]
            j -= 1
        # Place element i
        l[j + 1] = key
    return l


"""
Maintains sorted left sub-array, and repeatedly selects the minimum element from the unsorted
sub-array to place at the end of the left sub-array
O(n^2)
"""
def selection_sort(l: list) -> list:
    for i in range(len(l) - 1):
        # Find minimum element index in remaining sub-array
        min_i = i
        for j in range(i+1, len(l)):
            if l[j] < l[min_i]:
                min_i = j
        # Swap min element with start of unsorted sub-array
        l[i], l[min_i] = l[min_i], l[i]
    return l






l = [4, 3, 2, 7, 8, 1, 5, 6]
# print(insertion_sort(l))
print(selection_sort(l))