a=int(input('Enter a: '))
output=[ i*2+1 for i in range(a)]
print(','.join(map(str,output)))

