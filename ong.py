def fact(numero):
    i  =   1    
    num   =   1
    while (i <= numero):
        num = num * i
        i = i + 1
    return (num)        

def prod(*args):
    num=(len(args))  
    i   =   0    
    p   =   1
    while (i <= (num-1)):
        p = p * args[i]
        i = i + 1
    return (p)   
    

b   =   fact (5)
c   =   prod (4, 6, 7, 4, 3)  
d   =   fact (6)
print(b,c,d)
