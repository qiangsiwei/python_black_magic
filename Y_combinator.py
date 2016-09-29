import sys

# https://en.wikipedia.org/wiki/Fixed-point_combinator#Fixed_point_combinators_in_lambda_calculus

y1 = lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args)))

def factorial(fac):
    return lambda n: n if (n<=2) else n*fac(n-1)

def fix(func):
    b = (lambda f: (lambda x: x(x))(lambda y: f(lambda *args: lambda: y(y)(*args))))(func)
    def wrapper(*args):
        out = b(*args)
        while callable(out):
            out = out()
        return out
    return wrapper

@fix
def fact(f):
    return lambda n,r: r if n<2 else f(n-1, n*r)

if __name__ == "__main__":
    print fact(100,1)
    