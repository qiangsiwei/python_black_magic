import sys

class TailRecurseException:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs

def tail_recurse(g):
    def func(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
            raise TailRecurseException(args, kwargs)
        else:
            while 1:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException, e:
                    args = e.args
                    kwargs = e.kwargs
    return func

def fact1(n):
    if n == 0:
        return 1
    else:
        return n*fact1(n-1)

@tail_recurse
def fact2(n, r=1):
    if n == 0:
        return r
    else:
        return fact2(n-1, n*r)

def fb1(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fb1(n-1)+fb1(n-2)

@tail_recurse
def fb2(n, current=1, next=1):
    if n == 0:
        return current
    else:
        return fb2(n-1, next, current+next)

if __name__ == "__main__":
    # print fact1(1000)
    # print fact2(1000)
    # print fb1(1000)
    # print fb2(1000)
    pass
    