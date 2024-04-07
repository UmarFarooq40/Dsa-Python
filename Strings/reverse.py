#Reverse a String

st='My name is umar'
n=len(st)
def reverse():
    res=''
    for i in st:
       res=i+res
    return res
print(reverse())


#Reverse Words in string:

string='My name is umar'
st=string.split(' ')
def RevWords():
    l=[]
    for word in st:
           l.append(word[::-1])
    return ' '.join(l)
print(RevWords())

