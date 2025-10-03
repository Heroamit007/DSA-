class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self,item):       
            self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("empty queue")
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("empty queue")
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("empty queue")
    def size(self):
        return len(self.items)


#driver code
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
print("Item at the front is",q.get_front())
q.enqueue(40)
print("Item at the rear is", q.get_rear())
