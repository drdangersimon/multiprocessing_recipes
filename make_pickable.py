


from __future__ import (division, print_function, absolute_import,
                        unicode_literals)
import cPickle as pik

class function_wrapper(object):
    """From https://raw.githubusercontent.com/dfm/emcee/master/emcee/ensemble.py
    This is a hack to make the function pickleable when ``args``
    or ``kwargs`` are also included.

    """
    def __init__(self, f, args, kwargs):
        self.f = f
        self.args = args
        self.kwargs = kwargs

    def __call__(self, x):
        try:
            return self.f(x, *self.args, **self.kwargs)
        except:
            import traceback
            print("  params:", x)
            print("  args:", self.args)
            print("  kwargs:", self.kwargs)
            print("  exception:")
            traceback.print_exc()
            raise
