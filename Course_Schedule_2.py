'''
Problem from Leetcode
Several of the testcases were in conflict with the statements made in the question description, so this did not pass all of the testcases
'''

class Solution:

    def findOrder(self, numCourses, prerequisites):

        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # Create an adjacency list
        adj_list = [[] for i in range(numCourses)]

        # Fill in the adjacency list for each directed edge (b -> a)
        for [a, b] in prerequisites:
            adj_list[b].append(a)

        # Create the LIFO queue for BFS
        queue = []

        # Find node to begin search from
        i = 0
        while len(queue) == 0 and i < numCourses:
            if len(adj_list[i]) > 0:
                queue.append(i)
            i += 1

        # Keep track of the path
        path = []

        # Keep track of the explored nodes
        explored = []

        # Keep trying paths until no options are left
        while len(queue) > 0:

            # Make the next node the last one in the list
            curr_node = queue.pop(0)

            # Add the node to the path
            path.append(curr_node)

            # Add the node to the explored list
            explored.append(curr_node)

            # Find the potential next nodes
            next_nodes = adj_list[curr_node]

            # Error state if only one option exists and it loops back to an explored node
            if len(next_nodes) == 1 and next_nodes[0] in explored:
                path = []
                return path

            # If the next nodes have not already been explored, add them to the queue
            for next_node in next_nodes:

                if next_node not in explored and next_node not in queue:
                    queue.append(next_node)
        
        # If not all of the nodes had prerequisites, add them onto the front
        if len(path) < numCourses:
            for course in range(numCourses):
                if course not in path:
                    path.insert(0, course)

        return path
            















