class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        tempnode = self.head
        res = ''
        while tempnode is not None:
            res += str(tempnode.value)
            if tempnode.next is not None:
                res += '------->'
            tempnode = tempnode.next
        return res
#---------------> ADD A NODE AT THE END OF THE LL
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


#  INSERT A NODE AT ANY SPECIFIC INDEX ---------------------------------------------------------------->
    def insert(self, value, index):
        new_node = Node(value)
        # Case1: If you insert at negative index or at that index which is not present
        if index < 0 or index > self.length:
            return False
        # Case2: If Linked List is Empty
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # Case3: If You want to insert at the first position (ie Zero Index)
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            # Case 4 : If you want to insert at any specific position (SPECIFIC-INDEX)
            temp_node = self.head
            for _ in range(index - 1):  # for this loop Time Complexity O(n), rest all takes O(1)
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            # Update the tail if the new node is inserted at the end
            if new_node.next is None:
                self.tail = new_node
        self.length += 1
        return True
    
    
    # SEAERCHING WHEATHER THE NODE IS PRESENT OR NOT IF YES IT WILL RETURN TRUE ELSE IT WILL RETURN FALSE

    def search(self,target):
        current=self.head
        while current:
            if current.value==target:
                return True
            current=current.next
        return False
    

    # SERACHING AND RETURNING INDEX ------------------------------------------------->

    def search_Index(self,target):
        current = self.head
        index=0
        while current:
            if current.value==target:
                return index
            current=current.next
            index=index+1
        return -1
# Here we are passing the index  and getting the element at that index or node   
    def get(self,index):
        if index == -1 :
            return self.tail
        if index <-1 or index >= self.length:
            return None
        current=self.head
        for _ in range(index):
            current=current.next
        return current
  
# Set method is used to update the value of any given node
# based on the index
    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    
    def popFirst(self):
    #if we dont have any node in LL
        if self.length==0:
            return None
        popped_node=self.head
        # if we have only one Node in the Linked List
        if self.length==1:
            self.head=None
            self.Tail=None
        else:
            self.head=self.head.next
            popped_node.next= None
        self.length-=1 
        return popped_node
    
    def pop(self):
        if self.length==0:
            return None
        popped_node=self.tail
        if self.length==1:
            self.head=self.tail=None
        else:    
            temp=self.head
            while temp.next is not self.tail:
                temp=temp.next

            self.tail=temp
            temp.next=None
        self.length-=1
        return popped_node
    
    

    

     
   



# Test the LinkedList implementation
new = LinkedList()
new.append(2)
new.append(2)
new.insert(22, 2)
new.append(2)
new.append(7)

new.set_value(2,100)
print(new.search(22))
print(new.get(2).value)
print(new.length)  # Expected length: 5
print(new)  # Expected output: 2------->2------->22------->2------->7
print(new.search_Index(22))