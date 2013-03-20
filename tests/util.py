import nose

def tolerant(n=3):
    """ A decorator. If the wrapped test fails, try again a number of
times to see if we didn't just experience a network timeout.
"""

    def decorate(func):
        name = func.__name__

        def newfunc(*args, **kw):
            original_exception = None
            for i in range(n):
                try:
                    return func(*args, **kw)
                except Exception as e:
                    if not original_exception:
                        original_exception = e
                    if i is n-1:
                        raise original_exception

        newfunc = nose.tools.nontrivial.make_decorator(func)(newfunc)
        return newfunc
    return decorate
