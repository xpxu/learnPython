from functools import wraps

class lazy_property(property):
    """
    A property that works with subclasses by wrapping the decorated
    functions of the base class.
    """
    def __new__(cls, fget=None, fset=None, fdel=None, doc=None):
        '''fget=_get_do'''
        if fget is not None:
            # @wraps(fget)
            def fget(instance, instance_type=None, name=fget.__name__):
                return getattr(instance, name)()
        if fset is not None:
            # @wraps(fset)
            def fset(instance, value, name=fset.__name__):
                return setattr(instance, name)(value)
        if fdel is not None:
            # @wraps(fdel)
            def fdel(instance, name=fdel.__name__):
                return deleteattr(instance, name)()
        return property(fget, fset, fdel, doc)


class A(object):
    def _get_do(self):
        raise NotImplementedError

    def _set_do(self, value):
        raise NotImplementedError

    do = lazy_property(_get_do, _set_do)

class B(A):
    def _get_do(self):
        return "DO IT"


try:
    A().do
except NotImplementedError:
    print 'yes'

try:
    B().do
except NotImplementedError:
    print 'yes'
else:
    print 'no'



