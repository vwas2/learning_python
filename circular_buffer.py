import collections
import random
import timeit

import pytest


class Circular:
    """List-like store with benefit of O(1) at front modifications.
    (Currently) with a maximum length."""

    def __init__(self, maxlen: int):
        if maxlen <= 0:
            raise  # bad length
        self._list = [None] * maxlen
        self._front = None
        self._rear = None
        self._maxlen = maxlen

    @property
    def maxlen(self):
        return self._maxlen

    def _translate(self, i):
        """map index to internal_index of _list"""
        if self.isempty():
            return 0
        elif self._front <= self._rear:
            if self._front + i <= self._rear:
                return self._front + i
        else:
            if i < self._maxlen:  # non_modulo version
                if self._front + i < self._maxlen:
                    return self._front + i
                elif (self._front + i - self._maxlen) <= self._rear:
                    return self._front + i - self._maxlen
        return None

    def __getitem__(self, i: int):
        """return self[key]"""
        internal_index = self._translate(i)
        if internal_index is None:
            raise  # bad index
        return self._list[internal_index]

    def __setitem__(self, i: int, item):
        """set self[key] to value"""
        internal_index = self._translate(i)
        if internal_index is None:
            raise  # bad index
        self._list[internal_index] = item

    def isempty(self) -> bool:
        """check whether no items"""
        return self._rear is None and self._front is None

    def isfull(self) -> bool:
        """check whether maxlen items"""
        if self.isempty():
            return False
        return (self._rear + 1) % self._maxlen == self._front

    def append(self, item):
        """add item at rear"""
        if self.isfull():
            raise

        if self.isempty():
            self._front = self._rear = 0
            self._list[self._rear] = item
        else:
            internal_index = (self._rear + 1) % self._maxlen
            self._list[internal_index] = item
            self._rear = internal_index

    def appendleft(self, item):
        """add item at front"""
        if self.isfull():
            raise

        if self.isempty():
            self._front = self._rear = 0
            self._list[self._rear] = item
        else:
            if self._front >= 1:
                internal_index = self._front - 1
            else:
                internal_index = self._maxlen - 1

            self._list[internal_index] = item
            self._front = internal_index

    def pop(self):
        """remove and return item at rear"""
        if self.isempty():
            raise  # Empty

        item = self._list[self._rear]

        if self._front == self._rear:
            self._front = self._rear = None
        elif self._rear >= 1:
            self._rear -= 1
        else:
            self._rear = self._maxlen - 1

        return item

    def popleft(self):
        """remove and return item at front"""
        if self.isempty():
            raise  # Empty

        item = self._list[self._front]

        if self._front == self._rear:
            self._front = self._rear = None
        elif self._front + 1 < self._maxlen:
            self._front += 1
        else:
            self._front = 0

        return item


def test_constructor():
    with pytest.raises(Exception):
        Circular(0)

    c = Circular(1)
    assert c.maxlen == 1

    with pytest.raises(Exception):
        c.maxlen = 2


def test_isempty_isfull():
    c = Circular(2)
    assert c.isempty() is True
    assert c.isfull() is False

    c.append(10)
    assert c.isempty() is False
    assert c.isfull() is False

    c.append(11)
    assert c.isempty() is False
    assert c.isfull() is True

    with pytest.raises(Exception):
        c.append(12)

    c.pop()
    assert c.isempty() is False
    assert c.isfull() is False

    c.pop()
    assert c.isempty() is True
    assert c.isfull() is False


def test_frontstack():
    c = Circular(3)
    c.appendleft(0)
    c.appendleft(1)
    c.appendleft(2)
    assert c.popleft() == 2
    assert c.popleft() == 1
    assert c.popleft() == 0


def test_rearstack():
    c = Circular(3)
    c.append(0)
    c.append(1)
    c.append(2)
    assert c.pop() == 2
    assert c.pop() == 1
    assert c.pop() == 0


def test_queue():
    c = Circular(3)
    # forward
    c.appendleft(0)
    c.appendleft(1)
    assert c.pop() == 0
    assert c.pop() == 1

    # backward
    c.append(2)
    c.append(3)
    assert c.popleft() == 2
    assert c.popleft() == 3


def benchmark_front(c, values):
    for v in values:
        c.appendleft(v)
    for _ in values:
        _ = c.popleft()


def benchmark_front_list(c, values):
    for v in values:
        c.insert(0, v)
    for _ in values:
        _ = c.pop(0)


def benchmark_rear(c, values):
    for v in values:
        c.append(v)
    for _ in values:
        _ = c.pop()


def benchmark_getset(c, values, indices):
    for i, v in zip(indices, values):
        c[i] = v
    for i, v in zip(indices, values):
        _ = c[i]


if __name__ == '__main__':
    print('testing...', end='')
    test_constructor()
    test_isempty_isfull()
    test_frontstack()
    test_rearstack()
    test_queue()
    print('ok')

    # benchmark
    size = 100_000
    indices = [random.randint(0, size - 1) for _ in range(size)]
    values = [random.randint(0, 99) for _ in range(size)]
    repeats = 3
    print(f'benchmark... on size {size:_}', end='')

    front = timeit.timeit(lambda: benchmark_front(Circular(size), values), number=repeats)
    print(f'circular benchmark_front {front / repeats * 1000:.3f}ms')

    rear = timeit.timeit(lambda: benchmark_rear(Circular(size), values), number=repeats)
    print(f'circular benchmark_rear {rear / repeats * 1000:.3f}ms')

    c = Circular(size)
    for v in values: c.append(v)
    getset = timeit.timeit(lambda: benchmark_getset(c, values, indices), number=repeats)
    print(f'circular benchmark_getset {getset / repeats * 1000:.3f}ms')

    # Deque
    front = timeit.timeit(lambda: benchmark_front(collections.deque(maxlen=size), values), number=repeats)
    print(f'deque benchmark_front {front / repeats * 1000:.3f}ms')

    rear = timeit.timeit(lambda: benchmark_rear(collections.deque(maxlen=size), values), number=repeats)
    print(f'deque benchmark_rear {rear / repeats * 1000:.3f}ms')

    c = collections.deque(maxlen=size)
    for v in values: c.append(v)
    getset = timeit.timeit(lambda: benchmark_getset(c, values, indices), number=repeats)
    print(f'deque benchmark_getset {getset / repeats * 1000:.3f}ms')

    # List
    front = timeit.timeit(lambda: benchmark_front_list(list(), values), number=repeats)
    print(f'list benchmark_front_list {front / repeats * 1000:.3f}ms')

    rear = timeit.timeit(lambda: benchmark_rear(list(), values), number=repeats)
    print(f'list benchmark_rear {rear / repeats * 1000:.3f}ms')

    c = list()
    for v in values: c.append(v)
    getset = timeit.timeit(lambda: benchmark_getset(c, values, indices), number=repeats)
    print(f'list benchmark_getset {getset / repeats * 1000:.3f}ms')

    """
    testing... on size 1_000_000
    circular benchmark_front 3416.814ms
    circular benchmark_rear 3502.577ms
    circular benchmark_getset 3448.412ms
    
    deque benchmark_front 180.769ms
    deque benchmark_rear 179.473ms
    deque benchmark_getset 397399.976ms
    
    list benchmark_front_list aborted too long
    list benchmark_rear 172.203ms
    list benchmark_getset 375.755ms
    """
