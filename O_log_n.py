import random
import datetime

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

