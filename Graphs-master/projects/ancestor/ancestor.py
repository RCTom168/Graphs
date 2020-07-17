# Understand

# Plan

# Graphs Problem Solving
# Translate the problem
# Nodes: People
# Edges: When a child has a parent

# Build our graph, or just define get_neighbors

# Choose an Algorithm
# Either BFS or DFS

# If we use DFS, how would we know if DFS happened to be faster?

# import deque from collections

# class Queue():
#     def __init__(self):
#         self.queue = []
#     def enqueue(self, value):
#         self.queue.append(value)
#     def dequeue(self):
#         if self.size() > 0:
#             return self.queue.pop(0)
#         else:
#             return None
#     def size(self):
#         return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    def__init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
    
    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex):
        return self.vertices[vertex]

graph = Graph()

def build_graph_ancestors):
    for parent, child in ancestors:
        # parent = pair[0]
        # child = pair[1]

        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edg(child, parent)
    
    return graph

def earliest_ancestor(ancestors, starting_node):

    graph = build_graph(ancestors)

    s = Stack()

    visited = set()

    s.push([starting_node])

    longest_path = []
    aged_one = -1

    while s.size() > 0:
        path = s.pop()
        current_node = path[-1]

        # If path is longer, or path is equal but the id is smaller
        if len(path) > len(longest_path) or len(path) == len(longest_path):
            longets_path = path

        if current_node not in visited:
            visited.add(current_node)

            parents = graph.get_neighbors(current_node)

            for parent in parents:
                new_path = path + [parent]
                s.push(new_path)
    
    return longest_path[-1]
