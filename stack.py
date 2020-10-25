# Stack: A stack.
# Your implementation should pass the tests in stack.py.
# Andrew Hepworth

class Stack:
    def __init__(self):
        self.data = []
        pass
    
    def is_empty(self):
        return self.data == []

    def push(self, value):
        self.data.append(value)
    
    def pop(self):
        self.out()
        out = self.data[len(self.data)-1]
        self.data.pop()
        return out
    
    def peek(self):
        self.out()
        return self.data[len(self.data)-1]
    
    def out(self):
        if self.is_empty():
            raise IndexError("Index is out of bounds")
