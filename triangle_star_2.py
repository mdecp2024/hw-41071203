#help(range)
a=5
b=a*2+1
for i in range(1,b,2):
    move=round((b-i)/2)-1
    print(f'  '*move,end='')
    print('*'*i)