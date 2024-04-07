firstNum=0
SecondNum=1
print(firstNum,SecondNum,end='')

for i in range(10):
    fib=firstNum+SecondNum
    firstNum=SecondNum
    SecondNum=fib
    print(fib ,end=' ')

