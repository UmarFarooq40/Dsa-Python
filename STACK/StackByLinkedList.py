

class Node:
  def __init__(self,value=None):
     self.value=value
     self.next=next
class LinkedList:
    def __init__(self):
        self.head=None

    def __iter__(self):
       currNode=self.head
       while currNode is not None:
          yield currNode
          currNode=currNode.next

class Stack:
   def __init__(self):
      self.LinkedList=LinkedList()
    
   def __str__(self):
      values=[str(x.value) for x in self.LinkedList]
      return '\n'.join(values)
   
   def isEmpty(self):
      if self.LinkedList.head==None:
         return True
      else:
         return False
    
   def push(self,value):
      node=Node(value)
      node.next=self.LinkedList.head
      self.LinkedList.head=node

   def Pop(self):
      if self.isEmpty():
         return 'Empty Stack cant be poped'
      else:
         nodeValue=self.LinkedList.head.value
         self.LinkedList.head=self.LinkedList.head.next 
         return nodeValue
    
   def peek(self):
      if self.isEmpty():
         return "Empty"
      else:
         nodevalue=self.LinkedList.head.value
         return nodevalue
      
   def delete(self):
      self.LinkedList.head= None

customstack=Stack()
print(customstack.isEmpty())
customstack.push(1)
customstack.push(2)
customstack.push(3)
customstack.push(4)
print(customstack.delete())
print(customstack)
print('-------------------------')
print(customstack.Pop())
print(customstack.peek())
print(customstack.isEmpty())
         
      
            