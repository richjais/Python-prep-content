'''Given an array of even size N, task is to find minimum value that can be added to an element so that array become balanced. 
An array is balanced if the sum of the left half of the array elements is equal to the sum of right half.'''

class Solution:
    def minValueToBalance(self,a,n):
        #code here.
        left=sum(a[:n//2])
        right=sum(a[n//2:])
        return abs(left-right)