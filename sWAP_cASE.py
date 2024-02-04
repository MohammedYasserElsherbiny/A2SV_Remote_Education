def swap_case(s):
    new=""
    
    for ch in s:
        if ch.isupper():
            new+=ch.lower()
        else:
            new+=ch.upper()
            
    return new
            
        

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
