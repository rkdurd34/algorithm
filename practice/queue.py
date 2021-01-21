queue_list = [1,2,3,4,5]
def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]
    del queue_list[0]
    

enqueue(6)
dequeue()
print(queue_list)

def recursive(data):
    if data<0:
        print("ended")
    else:
        print(data)
        recursive(data-1)
        print("returned")
recursive(5)
stack_list = []
def push(data):
    stack_list.append(data)
def pop():
    data = stack_list[-1]
    print(data)
    del stack_list[-1]

for i in range(10):
    push(i)
print(stack_list)

for i in range(5):
    pop()
    
print(stack_list)

