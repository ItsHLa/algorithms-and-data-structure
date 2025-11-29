class Queue:
    # First in - First out
    def __init__(self):
        self.queue = []
    
    def __str__(self):
        return str(self.queue)
    
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return self.size() == 0
    
    def head(self):
        if self.is_empty():
            raise IndexError('Head from empty queue')
        return self.queue[0]
    
    def tail(self):
        if self.is_empty():
            raise IndexError('Tail from empty queue')
        return self.queue[-1]
    
    ## add to last position
    def enqueue(self, element):
        self.queue.append(element)
        return element
    
    ## remove from first position
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Dequeue from empty queue')
        return self.queue.pop(0)
    
try:
    queue = Queue()

    # enqueue elements
    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')
    queue.enqueue('d')
    print(queue)

    print(f'Head: {queue.head()}')
    print(f'Tail: {queue.tail()}')

    # dequeue first element
    print(queue.dequeue())
    print(queue)
    
    # dequeue all elements
    print(queue)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    
    print(f"is empty: {queue.is_empty()}")

    print(queue.size())
except Exception as e:
    print(f'Exception {e}')