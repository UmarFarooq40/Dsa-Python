#sort dictionary on the basis of keys
print('fIRST METHOD TO SORT BY KEYS')
#---------------------------------------------------------------------------------------------------------------------------------
d1={1:'umar',2:'mahi',3:'fasil',33:'anees',21:'jiberan'}
sortedDict=sorted(d1.items())
print(dict(sortedDict))

#second Method
print('SECOND METHOD TO SORT BY KEYS')
#---------------------------------------------------------------------------------------------------------------------------------
d1={1:'umar',2:'mahi',3:'fasil',33:'anees',21:'jiberan'}
sorteddictionary={k:v for k,v in sorted(d1.items(),key=lambda item:item[0])}
print(sorteddictionary)
#-------------------------------------------------------------------------------------------------------------------------------

print(' METHOD TO SORT BY vALUES')

#sort dictionary on the basis of values
d1={1:'umar',2:'mahi',3:'fasil',33:'anees',21:'jiberan'}
sorteddictionary={k:v for k,v in sorted(d1.items(),key=lambda item:item[1])}
print(sorteddictionary)