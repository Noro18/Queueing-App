class Queue:
    def __init__(self, max_size=None):
        self.queue = []
        self.max_size = max_size
    
    def enqueue(self, value):
        if self.max_size is None or len(self.queue) < self.max_size:
            self.queue.append(value)
        else:
            print("Queue nakonu!")

    def dequeue(self):
        if not self.isEmpty():
            item = self.queue.pop(0)
            print(f"elemento {item} hamos husi Queue")
            return item
        else:
            print("Queue mamuk")
            return None
    
    def peek(self):
        if not self.isEmpty():
            return self.queue[0]

        else:
            print("Queue mamuk")
            return None
    
    def isEmpty(self):
        return len(self.queue) <= 0

    def isFull(self):
        if self.max_size is not None:
            return len(self.queue) >= self.max_size
        else:
            return None

    def display(self):
        if not self.isEmpty():
            print("QUeue: ", self.queue)
        else:
            print("QUeue mamuk: ", self.queue)