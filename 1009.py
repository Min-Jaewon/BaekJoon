n=int(input())
answer=[0]*n
for i in range(n):
    a, b=tuple(map(int, input().split()))
    a_=a%10 if a%10!=0 else 10
    b_=b%4 if b%4!=0 else 4
    if a_==10:
        answer[i]=10
    else:
        answer[i]=a_**b_%10
for i in range(n):
    print(answer[i])

