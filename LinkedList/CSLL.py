class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

    def __str__(self):
        return str(self.value)    #-->to print the value from get method



class CSlinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0


    def __str__(self):
        temp_node=self.head
        res=''
        while temp_node is not None:
            res+=str(temp_node.value)
            temp_node=temp_node.next
            if temp_node == self.head:
                break
            res+= '-------------->'
        return res

 # add a node at the end of a circular singly linked list   


    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node

        else:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
        self.length +=1
# add a node at the begening of the circular singly linked list

    def prepend(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=new_node
        self.length+=1
# Add a node at any Index in the CLL
    def insert(self,index,value):
        new_node=Node(value)
        if index > self.length or index <0:
            raise Exception("OUT OF RANGE")
        if index ==0:
            if self.length ==0:
                self.head=new_node
                self.tail=new_node
                new_node.next=new_node
            else:
                new_node.next=self.head
                self.head=new_node
                self.tail.next=new_node
        elif index ==self.length:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
        else:
            temp_node=self.head
            for _ in range(index-1):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node
            self.length +=1

    def traversal(self):
        current=self.head
        while current is not None:
            print(current.value)
            current=current.next
            if current==self.head:
                break

    def search(self,target):
        current=self.head
        while current is not None:
            if current.value==target:
                return True
            current=current.next
            if current == self.head:
                break
        return False
    
    def get(self,index):
        if index == -1:
            return self.tail
        elif index < -1 or index >=self.length:
            return None
        current = self.head
        for _ in range(index):
                current=current.next
        return current
    
    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    
    def pop_first(self):
        popped_node=self.head
        if self.length==0:
            return None
        elif self.length==1:
            self.head=None
            self.tail=None
            return popped_node
        else:
            self.head=self.head.next
            self.tail.next=self.head
            popped_node.next=None
        self.length-=1
        return popped_node
    
    def pop(self):
        popped_node=self.tail
        if self.length == 0:
            return None
        elif self.length==1:
            self.head=self.tail=None
        else:
            temp=self.head
            while temp.next is not self.tail:
                temp=temp.next
            temp.next=self.head
            self.tail=temp
            popped_node.next=None
        self.length -=1
        return popped_node
    
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        elif index ==0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        prev_nod=self.get(index-1)
        popped_node=prev_nod.next
        prev_nod.next=popped_node.next
        popped_node.next=None
        self.length-=1
        return popped_node
    

    def delete_all_nodes(self):
        if self.length ==0:
            return
        self.tail.next=None
        self.head=None
        self.tail=None
        self.length=0


         




csll=CSlinkedList()
csll.append(20)
csll.append(2022)
csll.insert(2,202)
print(csll.get(1))
csll.set_value(0,999)
print(csll.pop_first())
csll.pop()
csll.remove(1)
print(csll)

