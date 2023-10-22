class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        # Sort the points based on the euclidean distance between the two points
        points.sort(key=lambda p: math.sqrt(p[0]**2 + p[1]**2))
        return points[:k]