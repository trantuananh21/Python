# from collections import deque

# # initialize the stack
# stack = deque(['a', 'b', 'c'])
# print('Initial stack: {}'.format(stack), end='\n\n')


# # add element to stack
# stack.append('d')
# print('Add element to stack: {}'.format(stack))

# # remove element from stack
# stack.pop()  # this method return the removed element
# print('Remove element from stack: {}'.format(stack), end='\n\n')

# # get value of element at the end of stack
# print('Get value of element from stack: {}'.format(stack[-1]))

# Đồ thị
graph = {
    0: [4],
    1: [2],
    2: [1],
    3: [4],
    4: [0, 3]
}

def is_connected_recursive(vertex1, vertex2, graph, visited):
    
    if vertex2 == vertex1:  # found the vertex
        return True

    # check that the current vertex is visited
    visited.add(vertex1)
    
    # check every adjacent vertices
    for vertex in graph[vertex1]:
        # if this vertex is not visited => visit every adjacent vertices from it and get finding result
        if vertex not in visited and is_connected_recursive(vertex, vertex2, graph, visited):
            return True
    
    # not found after visiting all possible vertices
    return False


def is_connected(vertex1, vertex2, graph):
    # initialize a set of visited vertices
    return is_connected_recursive(vertex1, vertex2, graph, set())

# driver code
print('{} is connected to {}: {}'.format(0, 3, is_connected(0, 3, graph)))
print('{} is connected to {}: {}'.format(4, 2, is_connected(4, 2, graph)))