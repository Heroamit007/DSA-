class stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("empty stack")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("empty stack")
    def size(self):
        return len(self.items)


#driver code
s = stack()
s.push(10)
s.push(20)
s.push(30)
s.pop()
print("Item at the end is",s.peek())