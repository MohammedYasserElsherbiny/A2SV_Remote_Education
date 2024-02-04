class Solution(object):
    def fizzBuzz(self, n):
        lst = ["" for _ in range(n)]
        for i in range(n):
            if (i+1)%15==0:
                lst[i]="FizzBuzz"
            elif (i+1)%3==0:
                lst[i]="Fizz"
            elif (i+1)%5==0:
                lst[i]="Buzz"
            else:
                lst[i]=str(i+1)
        return lst
        
