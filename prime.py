def palindrome(l):
    x=[]
    for i in l:
            for j in range(2,i):
                if(i%j)==0:
                    break
                else:
                    x.append(i)
                    
    return list(set(x))

