#n = eval(input())
#for i in range(n-1):
#    print(i,end=',')
#print(n-1)
n=eval(input())
print(','.join(list(map(str,range(n)))))