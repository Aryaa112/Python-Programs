"""Problem: Reverse the given list in-place and also return a new reversed list. 
Approach: Use two-pointer technique or Python slicing. """

def reverse_arr(arr1):
    return arr1[::-1]
    
def reverse_pointer(arr2):
    left,right = 0,len(arr2)-1
    while(left<right):
        left,right = right,left
        left += 1
        right -=1
    return arr2

arr = list(map(int, input().split()))
print("First Reverse: ",reverse_arr(arr))
print("First Reverse: ",reverse_pointer(arr))
