class ArrayQueue:
    def __init__(self, capacity):
        self._data = [None] * capacity
        self._size = 0
        self._front = 0
        self.capacity = capacity
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def enqueue(self, e):
        if self._size == self.capacity:
            print("Queue is full")
            return
        avail = (self._front + self._size) % self.capacity   # Index where the next element is added to the queue
        self._data[avail] = e
        self._size += 1
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        answer = self._data[self._front]
        self._data[self._front] = None                       # Help garbage collection
        self._front = (self._front + 1) % self.capacity      # Circular indexing
        self._size -= 1                                      # Reduce the queue size
        return answer
    def display(self):
        if self.is_empty():
            return ""
        elements = []
        for i in range(self._size):
            idx = (self._front + i) % self.capacity
            elements.append(str(self._data[idx]))
        return " -> ".join(elements)
    

if __name__ == "__main__":
    n_str = input("Enter N: ")
    n = int(n_str)
    Q = ArrayQueue(n)

    nums_str = input(f"Enter {n} integers: ").split()
    for num in nums_str:
        Q.enqueue(int(num))

    pos_queue = ArrayQueue(n)                               # New Queues for positives
    neg_queue = ArrayQueue(n)                               # New Queues for negatives
    
    while not Q.is_empty():                                 # if val == 0, deletes the value 
        val = Q.dequeue()
        if val > 0:                                         # if val > 0, add to positives queue
            pos_queue.enqueue(val)
        elif val < 0:                                       # if val < 0, add to negative queue
            neg_queue.enqueue(val)
        
    print(f"Positives Queue: {pos_queue.display()}")
    print(f"Negatives Queue: {neg_queue.display()}")
        