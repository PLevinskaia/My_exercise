dic={}
cid={}
n=int(input())
for i in range(n):
    child, *parent = input().replace(' : ', ' ').split(' ')
    if not parent:
        pass
    for par in parent:
        if par not in dic.keys():
            dic[par]=[]
        dic[par].append(child)
for k in dic.keys():
    cid[k]=dic[k]
    for l in dic[k]:
        if l in dic.keys():
            for m in dic[l]:
                if m not in cid[k]:
                    cid[k].append(m)
och=[]
m=int(input())
for i in range(m):
    ex = str(input())
    if ex in och:
        print(ex)
    if ex in cid.keys():
        for j in cid[ex]:
            if j not in och:
                och.append(j)
