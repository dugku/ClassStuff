import random
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    

def gen_matrix(m, n):
    return [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]

def main():

    A = [
        [1,1,1,0,1],
        [0,0,1,0,0],
        [1,1,1,1,1],
        [1,1,0,1,1],
        [1,1,0,1,1],
    ]
    pathDFS = DFS(A)
    pathBFS = BFS(A)

    if pathDFS == -1:
        print("No Path")
    else:
        print("DFS Path:")
        print(" -> ".join(map(str, pathDFS)))

    if pathBFS == -1:
        print("No Path")
    else:
        print("BFS Path:")
        print(" -> ".join(map(str, pathBFS)))

def DFS(A):
    s = Stack()

    m = len(A)
    n = len(A[0])

    goal = (m-1,n-1)

    directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
    i = 0
    j = 0
    
    visted = {}

    s.push(((i, j), []))
    visted[(i,j)] = True


    while s.isEmpty() != True:
        (i, j), path  = s.pop()

        if (i, j) == goal:
            return path
        
        for _, (dx, dy) in enumerate(directions):
            new_i = i + dx
            new_j = j + dy
            if 0 <= new_i < m and 0 <= new_j < n and A[new_i][new_j] == 1 and (new_i, new_j) not in visted:
                s.push(((new_i, new_j), path + [(new_i,new_j)]))
                visted[(new_i,new_j)] = True 
    return -1
def BFS(A):
    q = Queue()

    m = len(A)
    n = len(A[0])

    goal = (m-1, n-1)

    directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
    i = 0
    j = 0

    visted = {}

    q.enqueue(((i, j), []))
    visted[(i,j)] = True

    while not q.isEmpty():
        nade = q.dequeue()
        (i, j), path = nade

        if (i, j) == goal:
            return path

        for _ , (dx, dy) in enumerate(directions):
            new_i = i + dx
            new_j = j + dy

            if 0 <= new_i < m and 0 <= new_j < n and A[new_i][new_j] == 1 and (new_i, new_j) not in visted:
                visted[(new_i, new_j)] = True
                q.enqueue(((new_i, new_j), path + [(new_i, new_j)]))
    return -1


if __name__ == "__main__":
    main()