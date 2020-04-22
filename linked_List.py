# class Node:
#     def __init__(self,data, next=None):
#         self.data = data
#         self.next = next
# def add(data):
#     print('add function 실행!')
#     node = head
#     print(head.data, head.next ,'function 이후 head')
#     print(node.data, head.next, 'function 이후 node')
#     while node.next:
#         print(node.data,node.next)
#         node  = node.next
#         print(node.data,node.next,"와일문 지나고나서입니다")
        
#     print('while문 끝')   
#     node.next = Node(data)
#     print(node.data,node.next)
#     print(head.data,head.next)

# node1 = Node(1)
# head = node1

# for i in range(2,10):
#     print(head.data, head.next,"for문 시작 전 head 입니다")
#     print("for문 시작", i, '이것은 포문 i')
    
#     add(i)
#     print(head.data,head.next, "head 입니다")
    
#     print("for문 끝")


# node_1= Node(1)
# node_2 = Node(2)
# node_1.next = node_2
# head_1 = node_1
# print(head_1.data,head_1.next,head_1.next.data,head_1.next.next)


# node1 = Node(1,None)
# head = node1
# for index in range(2,10):
#     add(index)

# class Node:
#     count = 0
#     def __init__(self,data, next=None):
#         self.data = data
#         self.next = next
#         Node.count += 1
# def add(data):
#     node = head
#     # print(node.data, node.next, head.data ,head.next)
#     while node.next:
#         node = node.next
#     print(node.next)
#     node.next = Node(data)
#     return node.next
#     # print(node.next,  Node(data))
#     # print(node.data, node.next, head.data ,head.next)

# node1 = Node(1)
# head = node1
# for index in range(2,10):
#     print(add(index))
# print(Node.count)

# print('여기서 시작')
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class NodeMgmt:
    def __init__(self,data):
        self.head = Node(data)

    def add(self,data):
        if self.head == "":
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
    def delete(self,data):
        if self.head =="":
            print("해당 값을 가진 노드가 없습니다")
            return
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next 
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    print('wldna')
                    return
                else:
                    node = node.next
    def search_node(self,data):
        node = self.head
        if node == "":
            print('리스트가 비어있습니다')
        else:
            while node:
                if node.data == data:
                    return print(node.next.data)
                node = node.next

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
linked_list_3 = NodeMgmt(0)
for i in range(1,10):
    linked_list_3.add(i)
linked_list_3.delete(9)
linked_list_3.desc()
linked_list_3.search_node(4)

print()
print('Double_linked_list 시작')
class Node:

    def __init__(self,data,prev=None, next=None):

        self.prev = prev
        self.data =data
        self.next = next
class NodeMgmt:
    def __init__(self,data):
        self.head = Node(data)
        self.tail = self.head
    def insert(self,data):
        if self.head == None:
            self.head =Node(data)
            self.tail = self.head
            return
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    def search_from_head(self,data):
        if self.head == None:
            return False
        else:
            node = self.head
            while node:
                if node.data == data:
                    return node
                else:
                    node= node.next
    def insert_after_kang(self,data,after_data):
        print('tl')
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            return
        else:
            node = self.head
            while node:
                if after_data == node.data:
                    if node == self.tail:
                        print('tail case')
                        new = Node(data)
                        node.next = new
                        new.prev = node
                        return
                    else:
                        print('rest')
                        new = Node(data)
                        new.prev = node
                        new.next = node.next
                        node.next.prev = new
                        node.next = new
                        return
                node = node.next
    def insert_after(self,data,after_data):
        if self.head ==None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while after_data != node.data:
                node =node.next
                if node == None:
                    return False
            new = Node(data)
            new.prev = node
            new.next = node.next
            node.next =new
            node.next.prev = new



    def insert_before(self, data ,before_data):
            node = self.tail
            while before_data  != node.data:
                node = node.next
                if before_data !=self.tail.data:
                    return False
            new = Node(data)
            new.prev = node



double_linked_list1= NodeMgmt(1)
for i in range(2,10):
    double_linked_list1.insert(i)
double_linked_list1.desc()
print()
double_linked_list1.insert_after(3,2)

double_linked_list1.desc()


                    



                    

                
        


                
            



        

