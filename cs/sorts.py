# Bubble sort

# Bubble sort goes through elements and compares adjacent elements -- if one element is bigger than the adjacent, it swaps them in place
def bubblesort(myList): # Define function
    for i in range (0, len(myList)-1): # First placekeeping step --> this is saying, go through a list to the end of the list, no matter how long it is and i in each iteration will be the current position we are at
        for j in range (0, len(myList)-1-i): # Second placeholder step --> this is saying for the current spot where we are at (subtracting i just gets you at the i spot of the list)
            if myList[j] > myList[j+1]: # If what is at this current position is larger than the thing at the adjacent postion then...
                myList[j], myList[j+1] = myList[j+1], myList[j] # Swap definition -- just replaces one order with another!
    return myList

# Big O notation worst case: O(n^2) because you'd go through it the number of elements there are in the list
# Test it
myList = [0,1,2,3,4,5,6,7,8,9,10]
bubblesort(myList)

# If you wanted to go the opposite way:
def bubblesort_opp(myList):
    for i in range (0, len(myList)-1):
        for j in range (0, len(myList)-1-i):
            if myList[j] < myList[j+1]:
                myList[j], myList[j+1] = myList[j+1], myList[j]
    return myList

bubblesort_opp(myList)

# Merge sort

# Merge sort is a 'divide and conquer' algorithm. Divides array into two halves, calls itself in the half and merges the sorted halves
# Breaks things into two and works left from right to swap and arrange things
# Big O notation of merge sort is O(n log n)

def mergeSort(alist):
    print('Splitting ', alist)
    if len(alist)>1: # Saying if this list is bigger than one element...
        mid = len(alist)//2 # Figure out what the midpoint is
        lefthalf = alist[:mid] # Then divide into two halves wherever that midpoint is
        righthalf = alist[mid:]

        mergeSort(lefthalf) # Function calls itself on each half, and then continues to divide things in 2 until we get to len is not more than 1
        mergeSort(righthalf) # Same for the right half, keep dividing until len is not more than 1

        i = 0 # Starting at 0 for each of these indexes
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf): # This is saying while whatever point we are starting at is less than the length of our substrings
            if lefthalf[i] < righthalf[j]: # If whatever is at position where we are starting is less than whatever is at start position of the other half
                alist[k] = lefthalf[i] # Then put in our new sorted string k whatever is at the starting position of lefthalf (because it's smaller than the right side thing)
                i = i + 1 # Advance our index 1 to look at the next set of things
            else:
                alist[k] = righthalf[j] # If it is not smaller than righthalf, it must be bigger so now we put whatever is in that righthalf spot in first position in k
                j = j + 1 # Advance our index counter 1
            k = k + 1 # Advance our main string counter of sorted stuff 1, because these two things have put the smallest thing in the first spot

        while i < len(lefthalf): # What this is doing is adding the other side in -- so if LH was the smaller one, i has advanced but not j and vise versa
            # So let's say LH was smaller than RH, so i has advanced 1 and k has advanced 1. So we'd skip this part (because i is not less than 1)
            alist[k]=lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf): # If we are going along with above example -- so j is still less than 1 because it hasn't been advanced
            alist[k] = righthalf[j] # So you put whatever is at j in the new k spot, which is 1 further along (because you've advanved k in an earlier step!)
            j = j + 1
            k = k + 1
    print ("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)

# Quick sort
# Like merge sort is divide and conquer but instead of splitting in half, chooses a PIVOT and partions the array around the pivot

########################
#### BINARY SEARCH #####
#######################

# Given a sorted array arr[] of elements, write a function to search a given element x in arr[]
# Linear search (just go thru string) would be O(n) --> that many elements
# Binary search divides and conquers so that is O(logn)
# Code for a recursive binary search:

# Returns INDEX of x in array if present, else -1
def binarySearch(arr, elem, start = 0, end = None):
    if end is None:
        end = len(arr) - 1 # Always start at the end of the array
    if start > end: # If start which would be the first element in our array is more than whatever end is (which is length of our array - 1)
        return False # Tells us... something? I guess if this is just an array of len 1?
    mid = (start + end) // 2 # This establishes a midpoint, so like... 2 + 4 which is 6 divided by two which is 3
    # Base case:
    if elem == arr[mid]: # If whatever is at the midpoint is the value we are looking for, give us the mid value
        return mid
    if elem < arr[mid]: # If the element is less than whatever it is at the midpoint
        return binarySearch(arr, elem, start, mid-1) # Then do a binary search starting one less than the mid
    return binarySearch(arr, elem, mid+1, end) # If else, then do a binary search of the external part
# This is recursive, so it will keep cutting things in half until it finds what it needs to find!

# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, x, start = 2, end = None)
result

# Iterative Solution
def binarySearch_iterative(arr, elem):
    start, end = 0, (len(arr)-1) # Start is set at 0 and end is set at length of array - 1 (to get index of end)
    while start <= end: # While start is less than or equal to end (as long as we have an array) --> This keeps looping thru / iterating until we find it!
        mid = (start + end) // 2 # Establish midpoint
        if elem == arr[mid]: # If the element we are looking for is at mid
            return mid # Return mid
        if elem < arr[mid]: # If the element is less than midpoint
            end = mid - 1 # End gets established as as midpoint minus 1 (breaks it up into a new array to search)
        else:
            start = mid + 1 # Look at other end of string
    return False

binarySearch_iterative(arr,x)
