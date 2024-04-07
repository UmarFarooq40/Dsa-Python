class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class SlinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
#ADDING VALUES AT THE END OF THE SSL
    def append(self,value):
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode
        self.length+=1
#ADDING VALUES AT THE BEGINING OF THE SSL
    def prepend(self,value):
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
        else:
            newnode.next=self.head
            self.head=newnode
        self.length+=1
#ADDING VALUES AT THE SPECIFIED INDEX OF SSL
    def insert(self,index,value):
        newnode=Node(value)
        if index<0 or index > self.length:
            return False
        if self.length==0:
            self.head=newnode
            self.tail=newnode
        elif index==0:
            newnode.next=self.head
            self.head=newnode
       
        else:
            tempnode=self.head
            for _ in range(index-1):
                tempnode=tempnode.next
            newnode.next=tempnode.next
            tempnode.next=newnode
        self.length+=1
        return True
#Traversing each node of Single Linked List
    def Traversal(self):
        current_node=self.head
        while current_node is not None:
            print(current_node.value)
            current_node=current_node.next

#String Representation
    def __str__(self):
        res=''
        tempnode=self.head
        while tempnode is not None:
            res+=str(tempnode.value)
            if tempnode.next is not None:
                res+='-------->'
            tempnode=tempnode.next
        return res

ss1=SlinkedList()
ss1.append(10)
ss1.append(100)
ss1.prepend(66)
ss1.append(210)
ss1.prepend(88)
ss1.insert(2,999)
print(ss1)
print(ss1.length)
ss1.Traversal()
