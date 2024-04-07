class Stack:
    def __init__(self,MaxSize):
        self.list=[]
        self.MaxSize=MaxSize
    
 
    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list==[]:
            return True 
        else:
            return False

    def isFull(self):
        if self.MaxSize==len(self.list):
            return True
        else:
            return False
    
    def Push(self,value):
        if  self.isFull():
            return 'Cannot be inserted STACK is full'
        else:
            self.list.append(value)
            return 'Element Has been Inserted'
        
    def pop(self):
        if self.isEmpty():
            return 'Cannot remove Values for Empty Stack'
        else:
           return self.list.pop()
        
    def peek(self):
        if self.isEmpty():
            return 'Cannot remove Values for Empty Stack'
        else:
            return self.list[len(self.list)-1]
        
    def delete(self):
        self.list=None
customStack=Stack(2)

print(customStack.isFull())
print(customStack.Push(10))
print(customStack.Push(10))
print(customStack.Push(110))
print(customStack.isFull())
print(customStack.isEmpty())
print(customStack.peek())