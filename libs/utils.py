from typing import TypeVar, Iterable


T = TypeVar("T")


def pairs(l: Iterable[T]) -> Iterable[tuple[T, T]]:
    a = iter(l)
    return zip(a, a)

def grouped(iterable: Iterable[T], n=2) -> Iterable[tuple[T, ...]]:
    "s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ..."
    return zip(*[iter(iterable)]*n)


def trans(s, d):
    for r in d.items():
        s = s.replace(*r)
    return s
    # Or a bit more functional:

    # from functools import reduce
    # trans = lambda s, d: reduce(lambda t, r: str.replace(t, *r), d.items(), s)

    # print(trans('foobar', {'foo': 'bar'}))


def discretize(i, incr=1):
    # pip install portion
    # data structure and operations for intervals
    import portion as P
    first_step = lambda s: (P.OPEN, (s.lower - incr if s.left is P.CLOSED else s.lower), (s.upper + incr if s.right is P.CLOSED else s.upper), P.OPEN)
    second_step = lambda s: (P.CLOSED, (s.lower + incr if s.left is P.OPEN and s.lower != -P.inf else s.lower), (s.upper - incr if s.right is P.OPEN and s.upper != P.inf else s.upper), P.CLOSED)
    return i.apply(first_step).apply(second_step)
