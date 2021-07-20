"""
Problem: MaxSumSubArray
Algorithm: Kadane's
Approach:
1) take two variables : MaxSoFar and MaxEndHere Initialise both to 0.
2) Now loop through each item one by one and add that to MaxEndHere.
3) If MaxEndHere < 0 set MaxEndHere = 0 Else if MaxEndHere > MaxSoFar then MaxSoFar = MaxEndHere.

"""

def maxSumArray(a,size):
    MaxSoFar,MaxEndHere = 0,0

    for i in range(size):
        MaxEndHere = MaxEndHere + a[i]
        if MaxEndHere > MaxSoFar:
            MaxSoFar = MaxEndHere
        if MaxEndHere < 0:
            MaxEndHere = 0
    return MaxSoFar

a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
print(maxSumArray(a,len(a)))

"""
Less comparison Approach
"""
def maxSumArrayLess(a,size):
    MaxSoFar,MaxEndHere = 0,0

    for i in range(0,size):
        MaxEndHere = MaxEndHere + a[i]
        
        if MaxEndHere < 0:
            MaxEndHere = 0
        elif MaxEndHere > MaxSoFar:  #comparing only for positive values because negative values can't be greater anyway.
            MaxSoFar = MaxEndHere
    return MaxSoFar

a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
print(maxSumArrayLess(a,len(a)))

"""
Handeling All Negative Number scenario
"""

def maxSubArraySum(a,size):
     
    max_so_far =a[0]
    curr_max = a[0]
     
    for i in range(1,size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)
         
    return max_so_far
 
# Driver function to check the above function
a = [-13, -3, -25, -20, -3,-2, -16, -23, -12, -5, -22, -15, -4, -7]

print("Maximum contiguous sum is" , maxSubArraySum(a,len(a)))