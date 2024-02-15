if __name__ == '__main__':
    N = int(input())
    
    ans=[]
    for i in range(N):
        command=input().split()
        if command[0] == "insert":
            ans.insert(int(command[1]),int(command[2]))
        elif command[0] == "print":
            print(ans)
        elif command[0] == "remove" and int(command[1]) in ans:
            ans.remove(int(command[1]))
        elif command[0] == "append":
            ans.append(int(command[1]))
        elif command[0] == "sort" and len(ans)>0:
            ans.sort()
        elif command[0] == "pop" and len(ans)>0:
            ans.pop()
        else:
            ans.reverse()
        
