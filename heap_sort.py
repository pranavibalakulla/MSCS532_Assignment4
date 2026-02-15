import random

def heapify(arr, heap_size, root_index):
    """
    Maintains the max-heap property for a subtree rooted at the given index.

    Parameters:
    arr (list): The list representing the heap.
    heap_size (int): The size of the heap.
    root_index (int): The index of the root of the subtree.

    Time Complexity:
    O(log n), where n is the number of elements in the heap.
    """
    largest = root_index
    left_child = 2 * root_index + 1
    right_child = 2 * root_index + 2

    # Check if left child exists and is greater than the root
    if left_child < heap_size and arr[left_child] > arr[largest]:
        largest = left_child

    # Check if right child exists and is greater than the largest so far
    if right_child < heap_size and arr[right_child] > arr[largest]:
        largest = right_child

    # If the largest element is not the root, swap and continue heapifying
    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]
        heapify(arr, heap_size, largest)


def heapsort(arr):
    """
    Sorts a list of elements in ascending order using the Heapsort algorithm.

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.

    Time Complexity:
    Best Case: O(n log n)
    Average Case: O(n log n)
    Worst Case: O(n log n)

    Space Complexity:
    O(1) auxiliary space (in-place sorting).
    """
    n = len(arr)

    # Step 1: Build a max-heap from the input array
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        # Move the current root (maximum) to the end
        arr[0], arr[i] = arr[i], arr[0]

        # Restore the max-heap property for the reduced heap
        heapify(arr, i, 0)

    return arr


arr = [random.randint(1, 100) for _ in range(10)]

print("Original array:")
print(arr)

sorted_arr = heapsort(arr)

print("Sorted array:")
print(sorted_arr)
