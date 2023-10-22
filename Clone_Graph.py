"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    visited = {} # Keep track of visited nodes

    def cloneGraph(self, node: 'Node') -> 'Node':

        # Check if node has parameters, if not return empty node
        if node == None:
            return node

        # If node is in the list of visited nodes return the node
        if node in self.visited:
            return self.visited[node]
        
        # Create a new node in the visited hashmap and give it new parameters
        self.visited[node] = Node(node.val, [])

        # Recursively call the function to perform a depth first search on all of the node's neighbors
        if node.neighbors:
            self.visited[node].neighbors = [self.cloneGraph(n) for n in node.neighbors]
        
        # Return the current node
        return self.visited[node]
