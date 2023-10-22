# Problem from HackerRank
# Hayden Feddock

class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adjacency_list = [[] for i in range(num_nodes)]
    
    def connect(self, node1, node2):
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)
    
    def find_all_distances(self, starting_node):
        
        # LIFO queue
        queue = []
        queue.append(self.adjacency_list[starting_node])
        
        # Hashmap to show explored nodes and their distances from the starting node
        distances = {}
        distances[starting_node] = 0
        
        # Explore the node at the top of the queue
        layer = 1
        while len(queue) > 0:
            
            # Pops the first node off to make the current node
            current_node = queue.pop(0)
            
            # Explore each node connected to the current node
            next_nodes = []
            for n in current_node:
                
                # Check if the node has already been added to the hashmap
                if n not in distances:
                    
                    # Calculate the distance if not yet explored
                    distances[n] = layer * 6
                    
                    # Add the next nodes to the queue if not yet explored
                    for next_node in self.adjacency_list[n]:
                        if next_node not in next_nodes:
                            next_nodes.append(next_node)
                    
            # Append the next nodes to the queue
            if len(next_nodes) > 0:
                queue.append(next_nodes)
            
            # Increment the layer
            layer += 1
            
        # Print out the result
        output = ""
        for i in range(self.num_nodes):
            
            if i == starting_node:
                continue
            
            if i in distances:
                output += str(distances[i])
            else:
                output += "-1"
                
            if i != (self.num_nodes - 1):
                output += " "
        print(output)
            
            
            
                
            



t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)


'''
Sample input:
2
4 2
1 2
1 3
1
3 1
2 3
2

Sample Output:
6 6 -1
-1 6
'''


'''
# Unit Tests
import unittest
class TestSolution(unittest.TestCase):
    def test(self):
        input = [0,1,2,4,6,5,3]
        obj = Solution
        self.assertEqual(obj.findMedian(input), 3)

if __name__ == '__main__':
    unittest.main()
'''