/**
 * // This is Sea's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Sea {
 *   public:
 *     bool hasShips(vector<int> topRight, vector<int> bottomLeft);
 * };
 */
#include <cmath>

class Solution {
public:
    int countShips(Sea sea, vector<int> topRight, vector<int> bottomLeft) {

        // If the bounds include less than one point, or if there are no ships in the space, return 0
        if (bottomLeft[0] > topRight[0] || bottomLeft[1] > topRight[1] || !(sea.hasShips(topRight, bottomLeft))) {
            return 0;
        
        // If there is one point and there must be a ship in it, return 1
        } else if (bottomLeft[0] == topRight[0] && bottomLeft[1] == topRight[1]) {
            return 1;
        }

        /* Break up plane into quadrants: upperLeft, upperRight, lowerLeft, lowerRight
        The boundaries are not equal to prevent double counting
            _____________________
            | Q1       |   Q2    |
            |          |         |
            |__________|_________|
            |          |         |
            | Q3       |    Q4   |
            |          |         |
            |__________|_________|

        */

        // Define the center values of the square
        int centerX = std::floor((bottomLeft[0] + topRight[0]) / 2);
        int centerY = std::floor((bottomLeft[1] + topRight[1]) / 2);

        // Using the center, topRight, and bottomLeft values to determine the top right and bottom left values for each quadrant
        vector<int> topRightQ1 = {centerX, topRight[1]};
        vector<int> bottomLeftQ1 = {bottomLeft[0], centerY + 1};

        vector<int> topRightQ2 = topRight;
        vector<int> bottomLeftQ2 = {centerX + 1, centerY + 1};

        vector<int> topRightQ3 = {centerX, centerY};
        vector<int> bottomLeftQ3 = bottomLeft;

        vector<int> topRightQ4 = {topRight[0], centerY};
        vector<int> bottomLeftQ4 = {centerX + 1, bottomLeft[1]};

        int ships = 0;
        // Check Q1 first
        ships += countShips(sea, topRightQ1, bottomLeftQ1);
        // Check Q2 second
        ships += countShips(sea, topRightQ2, bottomLeftQ2);
        // Check Q3 next
        ships += countShips(sea, topRightQ3, bottomLeftQ3);
        // Check Q4 last
        ships += countShips(sea, topRightQ4, bottomLeftQ4);

        // Return the number of ships
        return ships;
    }
};