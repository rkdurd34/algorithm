class Node:
    def __init__(self, key =None):

        self.key = key
        self.next = None
    def __str__(self):
        return str(self.key)

class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.size=0
# 빈 리스트 생성
    def PushFront(self,key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        self.size +=1
L = SinglyLinkedList() 