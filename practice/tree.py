class Node:
    def __init__(self,value):
        self.value = value
        self.left, self.right = None, None
class NodeMgmt:
    def __init__(self,head):
        self.head = head
    def insert(self,value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node= self.current_node.left
                else:
                    self.current_node.left =Node(value)
                    break
            if value >= self.current_node.value:
                # print(self.current_node.value, self.current_node.right)
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break
                    
    def search(self,value):
        self.current_node = self.head
        while self.current_node:
            if value == self.current_node.value:
                return self.current_node
                break
            if value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False
    def desc_right(self):
        self.current_node= self.head
        while self.current_node:
            if self.current_node.right != None:
                print(self.current_node.value)
                self.current_node = self.current_node.right
            else:
                print(self.current_node.value)
                print("the end")
                break
    def desc_left(self):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.left !=None:
                print(self.current_node.value)
                self.current_node = self.current_node.left
            else:
                print(self.current_node.value)
                print('the end')
                break
    def delete(self,value):
        self.current_node,self.parent = self.head,self.head
        searched = False
        while self.current_node:
            if value == self.current_node.value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            elif value > self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        if searched ==False:
            return False
        if self.current_node.right == None and self.current_node.left == None:
            if self.current_node.value > self.parent.value:
                self.parent.right == None
                del self.current_node
            else: 
                self.parent.left == None
                del self.current_node
        elif self.current_node.right == None or self.current_node.left ==None:
            



            

                

        

head = Node(1)
binary_tree =NodeMgmt(head)
for i in range(2,10):
    binary_tree.insert(i)
print(binary_tree.search(7).value)
binary_tree.desc_right()
binary_tree.desc_left()
