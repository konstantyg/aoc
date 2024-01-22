from time import perf_counter


def profiler(method):
    def wrapper_method(*arg, **kw):
        t = perf_counter()
        ret = method(*arg, **kw)
        t = perf_counter()-t
        print('Method ' + method.__name__ + ' took : ' +
              "{:2.9f}".format(t) + ' sec')
        return ret
    return wrapper_method
