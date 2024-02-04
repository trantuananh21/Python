from collections import deque

# initialize the stack
stack = deque(['a', 'b', 'c'])
print('Initial stack: {}'.format(stack), end='\n\n')


# add element to stack
stack.append('d')
print('Add element to stack: {}'.format(stack))

# remove element from stack
stack.pop()  # this method return the removed element
print('Remove element from stack: {}'.format(stack), end='\n\n')

# get value of element at the end of stack
print('Get value of element from stack: {}'.format(stack[-1]))