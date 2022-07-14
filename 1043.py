N, M=tuple(map(int, input().split()))
truth=list(map(int,(input().split())))

T=truth[0]
true_set=set(truth[1:])
answer=0
party_list=[]

for _ in range(M):
    party=list(map(int,(input().split())))
    party_member=set(party[1:])
    party_list.append(set(party_member))

for _ in range(M):
    for party in party_list:
        if party&true_set:
            true_set.update(party)

for party in party_list:
    intersection=party&true_set
    if len(intersection)==0:
        answer+=1
        
print(answer) 