dic={}
n=int(input())
for i in range(n):
    child, *parent = input().replace(':', ' ').split()


    print(child,parent)
    if child not in dic and parent:
        dic[child]=parent
        if len(parent)>1:
            for j in parent:
                dic[j]=parent[(parent.index(j)+1):]
print(dic)
zapros=[]
ban=[]
print(dic.values())
if 'BaseException' in dic.values():print('Da'[0])
if ['BaseException'] in dic.values():print('DaDa')
'''m=int(input())
for i in range(m):
    ex = input()
    zapros.append(ex)
    if ex in dic.values():
        ban.append()
        
def func():
    pass'''








