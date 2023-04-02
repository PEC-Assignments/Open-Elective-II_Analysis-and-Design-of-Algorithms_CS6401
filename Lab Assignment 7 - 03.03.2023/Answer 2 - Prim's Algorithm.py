# Solution to Question 2: Prim's Algorithm

# ---------------- MSB's Coding Template ---------------- #
'''
    "ɴᴏ ᴄᴏᴅᴇ ɪꜱ ᴘᴇʀꜰᴇᴄᴛ"
'''

# ---I/O from file---#
import sys
try:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    sys.stderr = open("output.txt", "w")
except:
    pass


# ---------------------- Code Starts Here ----------------------#

import sys


def prim(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    min_edge = [None, sys.maxsize]
    result = []
    min_edge[0] = -1
    key = [sys.maxsize] * num_vertices
    key[0] = 0

    for i in range(num_vertices):
        u = min_edge[0]
        visited[u] = True

        for v in range(num_vertices):
            if graph[u][v] and not visited[v] and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                min_edge = [u, v]

        result.append(min_edge)
        min_edge = [None, sys.maxsize]
        for v in range(num_vertices):
            if not visited[v] and key[v] < min_edge[1]:
                min_edge = [v, key[v]]

    return result


graph = [[0, 2, 0, 6, 0],
         [2, 0, 3, 8, 5],
         [0, 3, 0, 0, 7],
         [6, 8, 0, 0, 9],
         [0, 5, 7, 9, 0]]

result = prim(graph)
for u, v in result:
    print(f"{u} - {v}")
