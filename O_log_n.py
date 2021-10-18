import random
import datetime

# set time for test
start_time = datetime.datetime.now()

def binary_searcher(search_key, arr):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = int(low + (high-low)//2)
        if search_key == arr[mid]:
            return True
        if search_key < arr[mid]:
            high = mid-1
        elif search_key > arr[mid]:
            low = mid+1
    return False

# end time for test
end_time = datetime.datetime.now()
print(end_time - start_time)
