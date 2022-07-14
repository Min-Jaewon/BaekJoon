n=int(input())
RGB_list=[list(map(int, input().split())) for _ in range(n)] 

for i in range(1,n):
    RGB_list[i][0]+=min(RGB_list[i-1][1], RGB_list[i-1][2])
    RGB_list[i][1]+=min(RGB_list[i-1][0], RGB_list[i-1][2])
    RGB_list[i][2]+=min(RGB_list[i-1][0], RGB_list[i-1][1])
    
min_cost=min(RGB_list[n-1])
print(min_cost)