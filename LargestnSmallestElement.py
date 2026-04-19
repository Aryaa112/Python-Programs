"""Problem: Given a list of integers, find and return the largest element and smallest element 
Approach: Iterate through the list and keep track of maximum and minimum element. """

def largestnsmallest(l1):
    max = float("-inf")
    min = float("inf")

    if not l1:
        return None
        
    for i in range(len(l1)):
        if max < l1[i]:
            max = l1[i]
        elif min > l1[i]:
            min = l1[i]
    print("Largest Element : ", max)
    print("Smallest Element : ", min)
            
l1 = list(map(int, input().split()))
largestnsmallest(l1)

