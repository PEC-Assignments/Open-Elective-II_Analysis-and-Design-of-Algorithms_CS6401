# Solution to Question 2: Prim's Algorithm

# ---------------- MSB's Coding Template ---------------- #
"""
    "ɴᴏ ᴄᴏᴅᴇ ɪꜱ ᴘᴇʀꜰᴇᴄᴛ"
"""

# ---I/O from file---#
import sys

try:
    sys.stdin = open("input.txt", "r", encoding="UTF-8")
    sys.stdout = open("output.txt", "w", encoding="UTF-8")
    sys.stderr = open("output.txt", "w", encoding="UTF-8")
except FileNotFoundError as __:
    pass


# ---------------------- Code Starts Here ----------------------#
class Graph:
    """Class to represent a graph using adjacency matrix"""

    def __init__(self, vertices: int) -> None:
        """Constructor for Graph class

        Args:
            vertices (int): number of vertices in the graph
        """
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printMST(self, parent: list) -> None:
        """Function to print the constructed MST stored in parent[]

        Args:
            parent (list): list of parents of each vertex
        """
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def minKey(self, key: list[int], mstSet: list[bool]) -> int:
        """Function to find the vertex with minimum distance value,
        from the set of vertices not yet included in shortest path tree.

        Args:
            key (list[int]): list of keys of each vertex\n
            mstSet (list[bool]): list of boolean values to check if a vertex is in the MST

        Returns:
            int: index of the vertex with minimum distance value
        """
        minK = sys.maxsize
        min_index = 0
        for v in range(self.V):
            if key[v] < minK and mstSet[v] is False:
                minK = key[v]
                min_index = v
        return min_index

    def primMST(self) -> None:
        """Function to construct and print MST for a graph
        represented using adjacency matrix using Prim's Algorithm represented"""
        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        parent: list = [0] * self.V  # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1  # First node is always the root of

        for _ in range(self.V):
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)

            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if (
                    self.graph[u][v] > 0
                    and mstSet[v] is False
                    and key[v] > self.graph[u][v]
                ):
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)


# Driver's code
if __name__ == "__main__":
    ver = int(input("Enter the number of vertices: \n"))
    g = Graph(ver)
    print("Enter the adjacency matrix: ")
    g.graph = [list(map(int, input().split())) for i in range(ver)]

    g.primMST()

# Complexity Analysis of the above solution:
# Time Complexity: O(V^2).
# Space Complexity: O(V).

# Sample Input:
# 5
# 0 2 0 6 0
# 2 0 3 8 5
# 0 3 0 0 7
# 6 8 0 0 9
# 0 5 7 9 0
