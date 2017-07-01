def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    # Convert string to list, use loop over vowel list to remove, convert back
    y = list(s)
    x = list(s)
    v = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

    for char in y:
        for c in v:
            if c == char:
                x.remove(c)
            
    print(''.join(x))
