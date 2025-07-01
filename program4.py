a= [1,2,8,9,12,46,76,82,15,20,30]
output={}
for i in range(1,10):
    output[i]=0
    for j in a:
        if j%i==0:
            output[i]+=1
print(output)      