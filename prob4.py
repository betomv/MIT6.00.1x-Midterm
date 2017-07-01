def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """

    tri = [0]
    for i in range(1,100):
        tri.append(i+tri[-1])
    if k in tri:
        return True
    else:
        return False

