w="Yes"
    for i in a2:
        if i in a1:
            a1.remove(i)
        else:
            w="No"
            break
    
    return w
