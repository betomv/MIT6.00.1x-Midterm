def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''

    def sorting(li):
        x=[]
        y=[]
        for ele in li:
            if type(ele) == str:
                x.append(ele)
            if type(ele) == int:
                y.append(ele)
        x.sort()
        y.sort()
        final = x+y
        return final

    def stats(list1):
        count = 0
        most_times = None
        how_many = 0
        unique = []

        if list1 == []:
            return (None,None,None)
        
        for i in list1:
            if i not in unique:
                unique.append(i)
        for j in unique:
            unicount = 0
            for k in list1:
                if j == k:
                    unicount +=1
            if unicount > count:
                most_times = j
                count = unicount

        for l in list1:
            if most_times == l:
                how_many +=1

        what_type = type(most_times)
        result = (most_times,how_many,what_type)
        return result                      

    li1 = sorting(L1)
    li2 = sorting(L2)

    if li1 != li2:
        return False
    else:
        return stats(li1)
        

    
#EXAMPLES
L3 = [1, 'b', 1, 'c', 'c', 1]
L4 = ['c', 1, 'b', 1, 1, 'c']
print(is_list_permutation(L3,L4))
print(is_list_permutation([1, 2, '5', 2, 5, 3, 4, 4, 5, 5, 6], [3, 5, 1, '5', 2, 5, 2, 6, 4, 5, 4]))
print(is_list_permutation([],[]))
