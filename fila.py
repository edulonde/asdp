class Queue:

    def __init__(self):
        self.queue = []
        self.len_queue = 0

    def push(self,e):
        self.queue.append(e)
        self.len_queue +=1

    def pop(self):
        if not self.empty():
            self.queue.pop(0)
            self.len_queue -=1

    def empty(self):
        if self.len_queue == 0:
            return True
        return False

    def lenght(self):
        return self.len_queue

    def front(self):
        if not self.empty():
            return self.queue[0]

    def print(self):
        pass

q = Queue()
print(q.empty())
q.push(1)
q.push(2)
q.push(3)
remove()
print(q.front(),q.len_queue)
q.pop()
print(q.front(),q.len_queue)

