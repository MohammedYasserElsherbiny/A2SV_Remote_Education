n=int(input())
mp={}
for i in range(n):
    name, phone=input().split()
    mp[name]=phone

for i in range(n):
    try:
        w=str(input())
        if w in mp:
            print(w+'='+mp[w])
        else:
            print("Not found")
    except EOFError:
        break
