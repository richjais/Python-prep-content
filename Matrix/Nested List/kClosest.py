# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane
# and an integer k, return the k closest points to the origin (0, 0)

import math


def kClosest(points, k):
    res = []
    dist = []
    for point in points:
        dist.append([math.sqrt(point[0] ** 2 + point[1] ** 2), point])
    dist.sort(key=lambda x: x[0])
    for i in range(k):
        res.append(dist[i][1])
    return res


arr = [[1, 3], [-2, 2]]
print(kClosest(arr, 1))

# Approach---------------------------------------------------------------------------------------
# store distances of each point from origin along with point(dist), sort(dist) in ascending order,
# add points from (dist) list k times to output list
# Space Complexity: O(n)
# Time Complexity: O(n)
