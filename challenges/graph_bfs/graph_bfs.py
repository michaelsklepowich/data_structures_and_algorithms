import Graph from ./graph.py

def breadth_first_traversal(graph, start):
    """ this function takes a graph and a starting node and adds all vertecies of that
    node to a queue inside a loop, then marks that node as visited as to not repeat visits. 
    Then returns the visted set as output
    """
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited