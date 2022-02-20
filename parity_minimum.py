
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
m=min(arr)
res = list(map(int, str(m)))
sum=sum(res)

if (sum%2==0):
    print(1)
else:
    print(0)
