import collections


class Sdeque(collections.deque):
    """Add 'cut-slicing to the deque"""

    def __getitem__(self, item):
        if isinstance(item, slice):
            """add slicing support, but cut the slice out of the queue
            (Currently) limited to [a:b:+1] or [a:b:-1]
            """
            if item.start is None:
                start = 0
            elif item.start >= 0:
                start = item.start
            else:
                start = len(self) + item.start

            if item.stop is None:
                stop = len(self)
            elif item.stop >= 0:
                stop = item.stop
            else:
                stop = len(self) + item.stop

            if item.step in [1, -1]:
                step = item.step
            elif item.step is None:
                step = 1
            else:
                raise

            sublist = []
            if start > stop and step == -1:
                self.rotate(len(self) - start - 1)
                for _ in range(start - stop):
                    sublist.append(self.pop())
            elif start < stop and step == 1:
                self.rotate(-start)
                for _ in range(stop - start):
                    sublist.append(self.popleft())
            return sublist
        else:
            return super(Sdeque, self).__getitem__(item)


def test_slicing_sdeque(l):
    l_ref = list(l)
    assert l.copy()[:] == l_ref
    assert l.copy()[::] == l_ref
    assert l.copy()[:3] == l_ref[:3]
    assert l.copy()[1:3] == l_ref[1:3]
    assert l.copy()[1:4] == l_ref[1:4]
    assert l.copy()[-1:-4:-1] == l_ref[-1:-4:-1]
    assert l.copy()[1:-4:-1] == l_ref[1:-4:-1]


if __name__ == '__main__':
    q = Sdeque(i for i in range(10))
    print('testing Sdeque...', end='')
    test_slicing_sdeque(q)
    print('ok')
