#! /usr/bin/python

def my_reduce (bf, a, *z) :

#   check if v is omitted
    if (not a) and (not z)
        raise TypeError("reduce() of empty sequence with no initial value")

#   make sure a is iterable
    assert hasattr(a, '__iter__')

#   define interable using a
    p = iter(a)

    if not z:
        v = p.next()
    else:
        v = z[0]
    try :
        while True:
            v = bf(v, p.next())
    except StopIteration
        pass
    return v
