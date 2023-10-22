# Problem from HackerRank
# Hayden Feddock

import math
import os
import random
import re
import sys

#
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
#
class Solution:
    
    def componentsInGraph(gb):
        
        # Determine the number of nodes in graph
        num_nodes = 0
        for edge in gb:
            if edge[1] > num_nodes:
                num_nodes = edge[1]
        
        # Create the adjacency list
        adjacency_list = [[] for i in range(num_nodes)]
        for edge in gb:
            adjacency_list[edge[0] - 1].append(edge[1] - 1)
            adjacency_list[edge[1] - 1].append(edge[0] - 1)
        
        # For each node in the list, check the number of nodes it is connected to
        component_min = math.inf
        component_max = 0
        
        # Go through each node in the graph, and skip over nodes that have already been explored or are empty
        explored = {}
        for starting_node in range(num_nodes):
            
            # Check if the node has already been explored
            if starting_node in explored:
                continue
            
            # Check if the node is connected to anything
            if len(adjacency_list[starting_node]) == 0:
                explored[starting_node] = 1
                continue
        
            
            # Keep track of the number of nodes in the graph component
            component_nodes = 0
            
            # LIFO queue
            queue = []
            queue.append(adjacency_list[starting_node])
        
            # List to keep track of explored nodes
            component_explored = {}
        
            # Explore the node at the top of the queue
            while len(queue) > 0:
            
                # Pops the first node off to make the current node
                current_node = queue.pop(0)
            
                # Explore each node connected to the current node
                next_nodes = []
                for n in current_node:
                    
                    # Check if the node has already been added to the hashmap
                    if n not in component_explored:
                        
                        # Add the component to the explored hashmap
                        component_explored[n] = 1
                        explored[n] = 1
                        
                        # Increment the number of nodes in the sub graph
                        component_nodes += 1
                        
                        # Add the next nodes to the queue if not yet explored
                        for next_node in adjacency_list[n]:
                            if next_node not in next_nodes:
                                next_nodes.append(next_node)
                    
                # Append the next nodes to the queue
                if len(next_nodes) > 0:
                    queue.append(next_nodes)

            # If the number of nodes in the component is less than the min, update the min
            if component_nodes < component_min:
                component_min = component_nodes
            
            # If the number of nodes is greater than the max, update the max
            if component_nodes > component_max:
                component_max = component_nodes
                
        return [component_min, component_max]

# Unit Tests
import unittest
class TestSolution(unittest.TestCase):
    def test(self):
        input = [[1, 6],[2, 7], [3, 8], [4,9], [2, 6]]
        obj = Solution
        self.assertEqual(obj.componentsInGraph(input), [2, 4])

if __name__ == '__main__':
    unittest.main()