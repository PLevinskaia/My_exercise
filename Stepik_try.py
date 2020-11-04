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
#print(dic)
och=[]
flag=0
q=int(input())
for k in range(q):
    f,s=input().split()
    if s==f and s in dic:
        print('Yes')
    elif s!=f:
        for l in dic[s]:
            och.append(l)
        if len(och)==0:
            print('No')
        while len(och)!=0:
            if och[0]==f:
                print('Yes')
                #print('1',och)
                och = []
                break
            else:
                if och[0] in dic.keys():
                    for m in dic[och[0]]:
                        och.append(m)
                    och=och[1:]
                    #print('2',och)
        och = []