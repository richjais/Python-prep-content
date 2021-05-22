#Problem Description
'''Given an array arr[] of size N representing the size of candles which reduce by 1 unit each day. 
The room is illuminated using the given N candles. Find the maximum number of days the room is without darkness.'''

class Solution:
    def maxDays(self, arr, n):
        # code here
        max=arr[0]
        for elem in arr:
            if max<elem:
                max=elem
        return max
