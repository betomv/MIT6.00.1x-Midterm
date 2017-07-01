def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''

    result={}
    for i in d.values():
        
        if i not in result:
            result[i] = None
   
    for j in d.items():
        result[j[1]] = []
       
    for k in d.items():
        if k[1] in result:
            result[k[1]].append(k[0])
            result[k[1]].sort()

    return result
