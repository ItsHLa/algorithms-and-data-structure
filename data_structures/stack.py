class Stack:
    ## Last in - First out
      
    def __init__(self, *args, **kwargs):
        self._stack = []
    
    def size(self):
        return len(self._stack)
    
    # push into last position
    def push(self, element):
        self._stack.append(element)
        return element
    
    # push last element
    def pop(self):
        if self.is_empty():
            raise IndexError('Error pop from empty stack')
        return self._stack.pop()
    
    def top(self):
        if self.is_empty():
            raise IndexError('Error top from empty stack') 
        return self._stack[-1] # or size-1
    
    def is_empty(self):
        return self.size() == 0

    def __str__(self):
        return str(self._stack)
  
try:
    stack = Stack()

    # push elements
    stack.push('a')
    stack.push('b')
    stack.push('c')
    stack.push('d')

    print(f'Top: {stack.top()}')

    # pop elements
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()


    print(f'is empty: {stack.is_empty()}')
    print(stack)
    
except Exception as e:
    print(f'Exception : {e}')