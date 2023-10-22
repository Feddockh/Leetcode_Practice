'''
Each ship is located at an integer point on the sea represented by a cartesian plane, and each integer point may contain at most 1 ship.

You have a function Sea.hasShips(topRight, bottomLeft) which takes two points as arguments and returns true If there is at least one ship in the rectangle represented by the two points, including on the boundary.

Given two points: the top right and bottom left corners of a rectangle, return the number of ships present in that rectangle. It is guaranteed that there are at most 10 ships in that rectangle.

Submissions making more than 400 calls to hasShips will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification
'''


# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
class Point:
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y


class Sea:
    def  __init__(self, ships):
       self.ships = ships
    
    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
        for ship in self.ships:
            if (bottomLeft.x <= ship[0] and bottomLeft.y <= ship[1] and topRight.x >= ship[0] and topRight.y >= ship[1]):
                return True
        return False


# My solution
'''
class Solution:
    def countShips(self, sea, topRight, bottomLeft):
        # Return 0 if there are no ships
        if (bottomLeft.x > topRight.x or bottomLeft.y > topRight.y or sea.hasShips(topRight, bottomLeft)):
            return 0
        # Otherwise if there are ships and we have one point left, then return 1
        elif (bottomLeft.x == topRight.x and bottomLeft.y == topRight.y):
            return 1
        
        center = Point((topRight.x + bottomLeft.x) // 2, (topRight.y + bottomLeft.y) // 2)
        leftCenter = Point(bottomLeft.x, (topRight.y + bottomLeft.y) // 2)
        rightCenter = Point(topRight.x, (topRight.y + bottomLeft.y) // 2)
        bottomCenter = Point((topRight.x + bottomLeft.x) // 2, bottomLeft.y)
        topCenter = Point((topRight.x + bottomLeft.x) // 2, topRight.y)
        
        ships = 0
        # Check the bottom left quadrant
        ships += self.countShips(self, sea, center, bottomLeft)
        # Check the top right quadrant
        ships += self.countShips(self, sea, topRight, center)
        # Check the top left quadrant
        ships += self.countShips(self, sea, topCenter, leftCenter)
        # Check the bottom right quadrant
        ships += self.countShips(self, sea, rightCenter, bottomCenter)
        return ships
'''
# I could not get my solution to work unfortunately, and after awhile I decided to check the answer to see where I was going wrong
# I was quadruple counting some of the ships in the middle of the map becuase I had the points for the quadrants overlapping
# To fix this I was able to implement the method that the Leetcode solution showed where you add one to the middle to prevent the overlap issue


# Leetcode solution
class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        # If the current rectangle does not contain any ships, return 0.         
        if (bottomLeft.x > topRight.x) or (bottomLeft.y > topRight.y):
            return 0
        if not sea.hasShips(topRight, bottomLeft):
            return 0

        # If the rectangle represents a single point, a ship is located.
        if (topRight.x == bottomLeft.x) and (topRight.y == bottomLeft.y):
            return 1

        # Recursively check each of the 4 sub-rectangles for ships.
        mid_x = (topRight.x + bottomLeft.x) // 2
        mid_y = (topRight.y + bottomLeft.y) // 2
        return self.countShips(self, sea, Point(mid_x, mid_y), bottomLeft) + \
               self.countShips(self, sea, topRight, Point(mid_x + 1, mid_y + 1)) + \
               self.countShips(self, sea, Point(mid_x, topRight.y), Point(bottomLeft.x, mid_y + 1)) + \
               self.countShips(self, sea, Point(topRight.x, mid_y), Point(mid_x + 1, bottomLeft.y))
        # Add +1 to some dimensions in order to avoid double counting
        
# Note: I don't like how you have to pass the self object to itself when the function is not an __init__ function.
        
# Unit Tests
import unittest
class TestSolution(unittest.TestCase):
    def test1(self):
        ships = [[1, 1], [2, 2], [3, 3], [5, 5]]
        topRight = Point(4, 4)
        bottomLeft = Point(0, 0)
        obj = Solution
        self.assertEqual(Solution.countShips(obj, Sea(ships), topRight, bottomLeft), 3)
        
    def test2(self):
        ships = [[1, 1], [2, 2], [3, 3]]
        topRight = Point(1000, 1000)
        bottomLeft = Point(0, 0)
        obj = Solution
        self.assertEqual(Solution.countShips(obj, Sea(ships), topRight, bottomLeft), 3)

if __name__ == '__main__':
    unittest.main()