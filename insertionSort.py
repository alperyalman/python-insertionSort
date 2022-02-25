# insertionSort.py>

def insertionSort(input_array):
    sorted_array = list(input_array) # Copy and do not change the input array 
    print("Insertion sorting started")
    

    for i in range(1,len(input_array)):
        val = sorted_array[i]

        for j in range(i-1,-1,-1):
            if val < sorted_array[j]: # Check the value is smaller than the previous elements
                sorted_array[j+1] = sorted_array[j]
                sorted_array[j] = val
        print("{}. step: {}\n".format(i, sorted_array)) # Print each step
    return sorted_array