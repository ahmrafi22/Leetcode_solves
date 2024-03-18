class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        arrows = 1
        end = points[0][1]
    
        for start, point_end in points[1:]:
            if start > end:
                arrows += 1
                end = point_end
            else:
                end = min(end, point_end)
        
    
        return arrows