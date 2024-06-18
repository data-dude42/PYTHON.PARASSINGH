import random

def partition(data, low, high):
    """Partitions a sublist of a list using a randomly chosen pivot.

    Args:
        data: The list to be partitioned.
        low: The starting index of the sublist.
        high: The ending index (inclusive) of the sublist.

    Returns:
        The index of the pivot element in its final sorted position.
    """

    # Randomly choose a pivot from the sub-list
    pivot_index = random.randint(low, high)
    data[pivot_index], data[high] = data[high], data[pivot_index]

    i = (low - 1)
    pivot = data[high]  # Use a separate variable for the pivot value
    for j in range(low, high):
        if data[j] <= pivot:
            i = i + 1
            data[i], data[j] = data[j], data[i]
    data[i+1], data[high] = data[high], data[i+1]
    return (i+1)

def quickSort(data, low, high):
    """Sorts a list using the Quick Sort algorithm with random pivot selection.

    Args:
        data: The list to be sorted.
        low: The starting index of the sublist.
        high: The ending index (inclusive) of the sublist.
    """

    if low < high:
        partition_index = partition(data, low, high)
        quickSort(data, low, partition_index - 1)
        quickSort(data, partition_index + 1, high)

# Example usage
input_l = [9, 3, 5, 2, 6, 8, 6, 1, 3]
quickSort(input_l, 0, len(input_l) - 1)

print(input_l)
