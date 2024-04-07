
class Stack:
    def __init__(self):
        self.list=[]
        self.length=0
    

    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list==[]:
            return True
        return False


    
    def push(self,value):
        self.list.append(value)
        self.length+=1
        return 'The Element has been inserted'
        
    
    def pop(self):
        if self.isEmpty():
            return 'Empty Stack'
        else:
          self.list.pop()

    def peek(self):
        if self.isEmpty():
            return 'Empty stack'
        return self.list[len(self.list)-1]
    
    def delete(self):
        self.list=None
        return self.list
    # def list1(self):
    #     out=[]
    #     out.append(self)
    #     return out


customstack=Stack()

customstack.push(10)
customstack.push(100)
customstack.push(2100)
customstack.push(1101)
customstack.push(23100)
customstack.push(342100)
# print(customstack.pop())
print(customstack)
print('peek element')
print(customstack.peek())
print(customstack.delete())



