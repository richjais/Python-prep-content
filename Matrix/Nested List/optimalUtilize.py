# Given 2 lists a and b having elements as pair of integers
# first int represents unique ID and second int represents value
# find element from a and b such that sum of their values is less or equal to target(as close to target as possible)
# return ID of selected elements
# If no pair possible, return empty list

def findPairs(a, b, target):
    a.sort(key=lambda x: x[1])
    b.sort(key=lambda x: x[1])
    left = 0
    right = len(b) - 1
    diff = float('inf')
    res = []
    while left < len(a) and right >= 0:
        ID1, elem_a = a[left]
        ID2, elem_b = b[right]
        if target - elem_a - elem_b == diff:
            res.append([ID1, ID2])
        elif elem_a + elem_b <= target and target - elem_a - elem_b < diff:
            res.clear()
            res.append([ID1, ID2])
            diff = target - elem_a - elem_b
        if target > diff:
            left += 1
        else:
            right -= 1
    return res


a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7
print(findPairs(a, b, target))

# Approach
# Space complexity
# Time complexity