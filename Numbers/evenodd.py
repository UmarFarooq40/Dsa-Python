even=[]
odd=[]
for num in range(1,20):
    if num & 1==0:
        even.append(num)
    else:
        odd.append(num)
print(f'even numbers are{even}')
print(f'odd numbers are {odd}')