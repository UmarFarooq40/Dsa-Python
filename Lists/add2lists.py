list1=[10,20,200,100,50]
list2=[10,20,200,100,50]
list3=[10,20,200,100,50]
def Add():
    out=[]
    for i,j,k in zip(list1,list2,list3):
        out.append(i+j+k)
    return out
print(Add())
        