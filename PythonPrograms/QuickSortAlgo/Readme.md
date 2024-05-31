# **Quick Sort with Random Pivot Selection (Python Implementation)**

This code implements the Quick Sort sorting algorithm in Python with the following enhancements:

* **Random Pivot Selection:** Chooses a random pivot element from the sub-list to improve performance and avoid worst-case scenarios with already sorted or partially sorted data.

#### **Key Features:**

* Efficient sorting algorithm for large datasets.
* Average time complexity of O(n log n).
* Recursive implementation of Quick Sort.
* Employs a partition function to divide the sub-list around the pivot element.
* Uses random pivot selection for better performance.

#### **How to Use:**

1. Save the code as `quick_sort_randomized.py`.
2. Modify the `input_l` list at the bottom of the code to contain the unsorted data you want to sort.
3. Run the script from the command line using:

```
python quick_sort_randomized.py
```

#### **Explanation:**

* The `partition` function takes a sub-list of the data,`low` and `high` indices as input.
* It randomly selects a pivot element within the sub-list and swaps it with the last element (`high`).
* It iterates through the sub-list, comparing elements with the pivot.
* Elements less than or equal to the pivot are swapped to the left side of the sub-list.
* Finally, the pivot element is placed in its correct sorted position, and its index is returned.
* The `quickSort` function recursively sorts the sub-lists on either side of the pivot element in the original list.
* It checks if `low` is less than `high` to ensure there are elements to sort.
* It calls `partition` to position the pivot and obtain the partition index.
* It recursively calls itself to sort the left sub-list (`low` to `partition_index - 1`).
* It recursively calls itself to sort the right sub-list (`partition_index + 1` to `high`).

#### **Additional Notes:**

* This code demonstrates a basic recursive implementation of Quick Sort.
* For further optimization, you might consider:
  * **Hybrid Approach:** Combining Quick Sort with Insertion Sort for small sub-lists can improve performance.
  * **Tail Recursion Optimization:** Using iterative implementations or loop-based approaches for the smaller sub-list can avoid stack overflow errors in deep recursion scenarios (especially in languages without tail call optimization).

This implementation provides a well-explained and efficient Quick Sort algorithm with the benefit of random pivot selection for better handling of various data distributions.
