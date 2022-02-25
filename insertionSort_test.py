# Test insertionSort() function
from insertionSort import *

# Test input 1
unsorted_arr = [22,27,16,2,18,6]
print("Unsorted array is: {}\n".format(unsorted_arr)) # Print unsorted array first

# Get sorted array calling insertionSort() function
sorted_arr = insertionSort(unsorted_arr)
print ("Sorted array is: {}\n".format(sorted_arr))

# Test input 2
unsorted_arr = [7,3,5,8,2,9,4,15,6]
print("Unsorted array is: {}\n".format(unsorted_arr)) # Print unsorted array first

sorted_arr = insertionSort(unsorted_arr)
print ("Sorted array is: {}\n".format(sorted_arr))
