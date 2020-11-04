dic={}
n=int(input())
for i in range(n):
    a, *b = input().replace(':', '').split()
    if a not in dic:
        dic[a]=b
        for j in b:
            if j not in dic:
                dic[j]=[]
    else:
        for j in b:
            dic[a].append(j)
            for j in b:
                if j not in dic:
                    dic[j] = []
q=int(input())
def func_my(ff,ss):
    queue=dic[ss]
    while queue:
        if queue[0]==ff:
            return print('Yes')
        else:
            queue+=dic[queue[0]]
            queue = queue[1:]
    return print('No')
for k in range(q):
    f,s=input().split()
    if s in dic.keys():
        if s==f:
            print('Yes')
        else:
            func_my(f, s)
    else:
        print('No')
