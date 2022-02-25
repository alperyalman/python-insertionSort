# Python - Insertion Sort

## Files and descriptions

    insertionSort.py            Insertion sort algorithm takes unsorted array 
                                and outputs sorted array
    
    insertionSort_test.py       Test script
    

## Algorithm

```python
def insertionSort(input_array):
    sorted_array = list(input_array) # Copy and do not change the input array 
    print("Insertion sorting started")
    for i in range(1,len(input_array)):
        val = sorted_array[i]

        for j in range(i-1,-1,-1):
            if val < sorted_array[j]: # Check the value is smaller than the previous elements
                sorted_array[j+1] = sorted_array[j]
                sorted_array[j] = val
        print("{}. step: {} | {}\n".format(i,sorted_array[0:i],sorted_array[i:])) # Print each step
    return sorted_array
```

### __Test input 1__: [22,27,16,2,18,6]

    Unsorted array is: [22, 27, 16, 2, 18, 6]

    Insertion sorting started
    1. step: [22, 27, 16, 2, 18, 6]

    2. step: [16, 22, 27, 2, 18, 6]

    3. step: [2, 16, 22, 27, 18, 6]

    4. step: [2, 16, 18, 22, 27, 6]

    5. step: [2, 6, 16, 18, 22, 27]

    Sorted array is: [2, 6, 16, 18, 22, 27]


| Case      | Time Complexity   |
|-          | -                 |
| Best      | $O(n)$    |
| Average   | $O(n^2)$  |
| Worst     | $O(n^2)$  |

__Example__:
Sorted array is [2, 6, 16, 18, 22, 27]

If the number we are searching is 18, the corresponding case is ___Average case___ since the number is located in the middle of the sorted array.

---

### __Test input 2__: [22,27,16,2,18,6]

    Unsorted array is: [7, 3, 5, 8, 2, 9, 4, 15, 6]

    Insertion sorting started
    1. step: [3, 7, 5, 8, 2, 9, 4, 15, 6]

    2. step: [3, 5, 7, 8, 2, 9, 4, 15, 6]

    3. step: [3, 5, 7, 8, 2, 9, 4, 15, 6]

    4. step: [2, 3, 5, 7, 8, 9, 4, 15, 6]

    5. step: [2, 3, 5, 7, 8, 9, 4, 15, 6]

    6. step: [2, 3, 4, 5, 7, 8, 9, 15, 6]

    7. step: [2, 3, 4, 5, 7, 8, 9, 15, 6]

    8. step: [2, 3, 4, 5, 6, 7, 8, 9, 15]

    Sorted array is: [2, 3, 4, 5, 6, 7, 8, 9, 15]


