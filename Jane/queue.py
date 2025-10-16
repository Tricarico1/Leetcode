def memo_basic(f):

    dic = {}
    def g(n):
        if n in dic:
            return dic[n]
        else:
            dic[n]=f(n)
            return dic[n]
    return g