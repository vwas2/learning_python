class Solution(object):
    def canFormArray(self, arr, pieces):
        """leet_arrayformationcheck.py
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        i = 0
        length = len(arr)
        pieces_ = sorted(pieces, key=len, reverse=True)
        used = {tuple(p): False for p in pieces_}

        while i < length:
            for piece in pieces_:
                key = tuple(piece)
                if used[key]:
                    continue
                frag = arr[i:i + len(piece)]
                if frag == piece:
                    used[key] = True
                    i += len(piece)
                    break
            else:
                return False
        return True
        
    def numIdenticalPairs(self, nums):
        """leet_goodpairs.py
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        count = 0
        for i in range(length-1):
            v = nums[i]
            slc = nums[i+1:]
            count += slc.count(v)
        return count

    def reverse(self, x):
        """leet_intbackwards.py
        :type x: int
        :rtype: int
        """
        x_s = format(x, ' ')
        sign, x_digits_reversed = x_s[:1], x_s[-1:0:-1]
        v = int(sign + x_digits_reversed)

        if v < -2 ** 31 or v >= 2 ** 31:  # overflow
            return 0
        return v

    def romanToInt(self, s):
        """leet_introman.py
        :type s: str
        :rtype: int
        """
        numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000, }

        combinations = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }

        value = 0
        itr = iter(s + ' ') 
        for a, b in zip(itr, itr): 
            if a + b in combinations:
                value += combinations[a + b]
            else:
                value += numerals[a]
                value += numerals.get(b, 0)
        return value

    def isPalindrome(self, x):
        """leet_intsymmetric.py
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True

        q = x
        digits = []
        while q != 0:
            q, r = divmod(q, 10)
            digits.append(r)

        stop = len(digits) // 2  # drop midpoint
        f = digits[:stop]
        b = reversed(digits)

        for i, j in zip(f, b):
            if i != j:
                return False
        return True

    def maximum69Number(self, num):
        """leet_maximum69number.py
        :type num: int
        :rtype: int
        """
        s = str(num)
        maxed = s.replace('6', '9', 1)
        return int(maxed)

    def merge(self, intervals):
        """leet_mergeoverlappingintervals.py
        :type ll: List[List[int]]
        :rtype: List[List[int]]
        """
        ll = [l for l in intervals]
        if len(ll) < 2:
            return ll

        for i, _ in enumerate(ll):
            j = i
            j += 1
            while j < len(ll):
                start1, end1 = ll[i] # reread
                start2, end2 = ll[j]
                if start2 <= end1 and start1 <= end2:  # overlap
                    _ = ll.pop(j)
                    if start2 < start1:
                        ll[i] = [start2, ll[i][1]]  # no mutate
                    if end2 > end1:
                        ll[i] = [ll[i][0], end2]
                    j = i  # recheck
                j += 1

        return ll

    def checkPossibility(self, nums):
        """leet_mergeoverlappingintervals.py
        :type nums: List[int]
        :rtype: bool
        """
        corrections = 1
        length = len(nums)
        if length == 1:
            return True

        if nums[0] > nums[1]:
            nums[0] = nums[1]
            corrections -= 1

        for i in range(1, length - 1):
            if nums[i] > nums[i + 1]:
                if not corrections:
                    return False
                corrections -= 1
                decrease_i = nums[i - 1] <= nums[i + 1]
                if decrease_i:
                    nums[i] = nums[i + 1]
                else:  # fallback to increase i+1
                    nums[i + 1] = nums[i]
        return True

    def reverseKGroup(self, head, k):
        """leet_reversekgroup.py
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1: # speed, not cornercase
            return head
        lifo = []
        current = head
        while True:
            group_head = current
            for _ in range(k):
                if current is None:
                    return head
                lifo.append(current.val)
                current = current.next

            current = group_head
            for _ in range(k):
                current.val = lifo.pop()
                current = current.next
    
    def runningSum(self, nums):
        """leet_runningsum1d.py
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum = []
        for v in itertools.accumulate(nums):
            running_sum.append(v)
        return running_sum

    def shuffle(self, nums, n):
        """leet_shufflearray.py
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        half_length = len(nums) // 2
        shuffled = []
        for x, y in zip(nums[:half_length], nums[half_length:]):
            shuffled += [x, y]
        return shuffled

    # leet_subrectanglequeries.py:

    def __init__(self, rectangle):
        """
        :type rectangle: List[List[int]]
        """
        self._r = rectangle

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :type newValue: int
        :rtype: None
        """
        for row in range(row1, row2+1):
            for col in range(col1, col2+1):
                self._r[row][col] = newValue

    def getValue(self, row, col):
        """
        :type row: int
        :type col: int
        :rtype: int
        """
        v = self._r[row][col]
        return v

    ## END leet_subrectanglequeries.py;

    def numSub(self, s):
        """leet_substringsonly1s.py
        :type s: str
        :rtype: int
        """
        count = 0
        for k,g in it.groupby(s):
            if k == '0':
                continue
            for i,_ in enumerate(g): 
                count += i
        return count % (10**9 + 7) # leet requirement

    def threeSum(self, nums):
        """leet_threesum.py
        :type nums: List[int]
        :rtype: List[List[int]]

        time,space: On^2,On
        """
        # pruning input (if possible)
        counts = {}
        pruned = []
        for k, v in enumerate(nums):
            counts[v] = counts.get(v, 0) + 1
        for v, v_count in counts.items():
            counts = min(v_count, 3)
            for i in range(counts):
                pruned.append(v)

        length = len(pruned)
        solution = {}
        map_ = {v: k for k, v in enumerate(pruned)}
        for i in range(length):
            a = pruned[i]
            for j in range(i + 1, length):
                b = pruned[j]
                c = 0 - (a + b)
                k = map_.get(c, None)
                if j != k and i != k:
                    if k is not None:
                        triple = (a, b, c)
                        key = frozenset(triple)
                        solution[key] = triple  # overwrite previous permutation ok
        return list(solution.values())
    
    def twoSum(self, nums, target):
        """leet_twosum.py
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        time, space: On, <O2n
        """
        map_ = {}
        for i, v in enumerate(nums):
            j = map_.get(target - v)
            if j is not None and j != i:
                return [i, j]
            map_[v] = i


    def isValid(self, s):
        """leet_validparens.py
        :type s: str
        :rtype: bool
        """
        mapping = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        lifo = []

        for c in s:
            if c in mapping:
                right = mapping[c]
                lifo.append(right)
            else:
                if c in lifo[-1:]:
                    if c != lifo.pop():
                        return False
                else:
                    return False
        if len(lifo) != 0:
            return False
        return True

    def validSquare(self, p1, p2, p3, p4):
        """leet_validsquare.py
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        sdist = lambda p, q: (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
        distances = [] # squared
        distances += [sdist(p1, p2), sdist(p1, p3), sdist(p1, p4), ]
        distances += [sdist(p2, p3), sdist(p2, p4), ]
        distances += [sdist(p3, p4), ]

        distances_sorted = sorted(distances)
        hypo1 = distances_sorted.pop()
        hypo2 = distances_sorted.pop()
        sides = distances_sorted

        if sum(sides) > 0:
            equal = all(v == sides[0] for v in sides)
            if equal and hypo1 == hypo2:
                return True
        return False

    def subtractProductAndSum(self, n):
        """leet_productsumdigits.py
        :type n_: int
        :rtype: int
        """
        n_, r = divmod(n, 10)
        prod_ = r
        sum_ = r
        while n_ > 0:
            n_, r = divmod(n_, 10)
            prod_ *= r
            sum_ += r
        return prod_ - sum_


    def processQueries(self, queries, m):
        """1409. Queries on a Permutation With Key
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        l = collections.deque(range(1, m + 1))
        found = []
        for v in queries:
            # i = l.index(v)
            for i in range(m):  # >0
                if l[i] == v:
                    break
            found.append(i)
            l.rotate(-i)
            v = l.popleft()
            l.rotate(i)
            l.appendleft(v)

        return found        