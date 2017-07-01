def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """

    x = sorted(L)
    y=[]

    for i in x:
        if i not in y:
            y.append(i)
    num=0
    for j in y:
        count = 0
        
        for a in x:
            if j == a:
                count += 1
        if count % 2 != 0 and j > num:
            store = count
            num = j
            
        
    if num == 0:
        return None
    else:
       return num
