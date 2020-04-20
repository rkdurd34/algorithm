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






    
# class  Node:
#     def __init__(self,data,next=None):
#         self.data = data
#         self.next = next
# class  NodeMgmt:
#     def __init__(self,data):
#         self.head = Node(data)
#     def add(self,data):
#         if self.head =='':
#             self.head = Node(data)
#         else:
#             print("add ㅅ;작", data,"번쨰")
#             node = self.head
#             while  node.next:
#                 node = node.next
#             node.next = Node(data)
#     def desc(self):
#         node = self.head
#         while node:
#             print(node.data)
#             node = node.next

#     def delete(self,data):
#         if self.head =='':
#             print('해당 값을 가진 노드가 없습니다.')
#             return
#         if  self.head.data == data:
#             temp =  self.head
#             self.head = self.head.next
#             del temp
#         else:
#             node = self.head
#             while node.next:
#                 if node.next.data == data:
#                     temp = node.next
#                     node.next = node.next.next
#                     del temp
#                     return
#                 else:
#                     node = node.next
#     def search_node(self,data):
#         node=self.head
#         while node:
#             if node.data == data:
#                 return node
#             else:
#                 node = node.next


# linked_list1 = NodeMgmt(0)
# linked_list1.desc()
# for data in range(1,10):
#     linked_list1.add(data)
# linked_list1.desc()

# node1 = Node(1)     
# head = node1

# for i in range(2,10):
#     add(i)
# node3 =  Node(1.5)
# node =head
# # while node.next!=None:
# #     node = node.next
# search = True
# while search:
#     if node.data ==4 :
#         search = False
#     else:
#         node = node.next
# node_next =  node.next
# node.next =node3
# node3.next = node_next

# node =head
# while node.next!=None:
#     print(node.data)
#     node = node.next
# print(node.data)
    

