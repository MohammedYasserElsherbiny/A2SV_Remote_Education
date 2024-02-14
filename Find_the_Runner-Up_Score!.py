if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a=list(arr)
    a.sort()
    mx=-1000
    prev=0
    for i in range(len(a)):
        if a[i] > mx:
            prev=mx
            mx=a[i]
    print (prev)
    
