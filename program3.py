a=int(input('enter a: '))
b=a if a%2!=0 else a-1
output=[2*i+1 for i in range(b)]
print(','.join(map(str,output)))