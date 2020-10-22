```
Big-Oh notation
    - good for static analysis of your algorithm regards time complexity
      Q: What is the runtime growth as a function of input size n?
    - open to suggestions/edits
sources
    ...
    https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
    https://wiki.python.org/moin/TimeComplexity
    bigoh rules: Data Structures and Algorithms: Aho, Alfred, Ullman

```
|  method                                                                   | builtin types    |               |            |                 |
|---------------------------------------------------------------------|-----------|---------------|------------|-----------------|
| name                                                                | set       | dict          | list       | deque           |
| get(i)                                                              | -         | O(1), wc O(n) | O(1)       | O(1), mid O(n)  |
| set(i)                                                              | -         | O(1), wc O(n) | O(1)       | O(1), mid O(n)  |
| slicing                                                             | -         | -             | O(n)       | -               |
|                                                                     |           |               |            |                 |
| add(v)                                                              | O(1)      | -             | -          | -               |
| setdefault(k,[v])                                                   | -         | O(1)          | -          | -               |
| insert(v, i)                                                        | -         | -             | O(n)       | O(1), mid O(n)  |
| append(v)                                                           | -         | -             | O(1)       | O(1)            |
| appendleft(v)                                                       | -         | -             | -          | O(1)            |
| extend(vs), +=                                                      | -         | -             | O(1)       | O(1)+           |
| extendleft(vs)                                                      | -         | -             | -          | O(1)+           |
| update(vs), |=                                                      | O(1)      | O(1)          | -          | -               |
| multiply”, *                                                        | -         | -             | O(n)       | O(n)            |
|                                                                     |           |               |            |                 |
| index(v, [i,j])                                                     | -         | -             | O(n)       | O(n)            |
| count(v)                                                            | -         | -             | O(n)       | O(n)            |
|                                                                     |           |               |            |                 |
| delete()                                                            | O(1)?     | O(1)?         | O(n)       | O(n)            |
| remove(v)                                                           | O(1)?     | -             | O(n)       | O(n)            |
| discard(v)                                                          | O(1)?     | -             | -          | -               |
| pop(...)                                                            | O(1) ...- | O(1) ...k[,d] | O(n) ...i  | O(1) ...-       |
| popleft()                                                           | -         | -             | -          | O(1)            |
| popitem()                                                           | -         | O(1)          | -          | -               |
|                                                                     |           |               |            |                 |
| clear()                                                             | wc O(n)   | wc O(n)       | O(n)       | O(n)            |
| in                                                                  | O(1)      | O(1), wc O(n) | O(n)       | O(n)            |
| ’==,!=                                                              | O(n)      | O(n)          | O(n)       | O(n)+           |
| <,<=,>,>=                                                           | see below | -             | O(n)       | O(n)            |
| +                                                                   | O(1)      | -             | O(n)       | O(n)            |
| *                                                                   | -         | -             | O(n)       | O(n)            |
|                                                                     |           |               |            |                 |
| rotate(-+i)                                                         | -         | -             | -          | O(1)            |
| reverse()                                                           | -         | -             | O(n)       | O(n)            |
| sort()                                                              | -         | -             | O(n log n) | -               |
| copy()                                                              | O(n)      | O(n)          | O(n)       | O(n)            |
|                                                                     |           |               |            |                 |
|                                                                     |           |               |            |                 |
|                                                                     |           |               |            | wc:= worst case |
| ---- SET ONLY --------------------------------------------------    |           |               |            |                 |
| union(e), |; for inplace see .update()                              |           |               | O(1)       |                 |
| intersection(), &                                                   |           |               | O(1)       |                 |
| intersection_update(), &=                                           |           |               | O(1)       |                 |
| difference(), -                                                     |           |               | O(1)       |                 |
| difference_update(), -=                                             |           |               | O(1)       |                 |
| symmetric_difference(), ^                                           |           |               | O(1)       |                 |
| symmetric_difference_update(), ^=                                   |           |               | O(1)       |                 |
|                                                                     |           |               |            |                 |
| isdisjoint()                                                        |           |               | O(n)       |                 |
| issubset(), <=                                                      |           |               | O(n)       |                 |
| issuperset(), >=                                                    |           |               | O(n)       |                 |
| < proper subset                                                     |           |               | O(n)       |                 |
| > proper superset                                                   |           |               | O(n)       |                 |
|                                                                     |           |               |            |                 |
| ---- DICT ONLY --------------------------------------------------   |           |               |            |                 |
| .keys()                                                             |           |               | O(1)       |                 |
| .values()                                                           |           |               | O(1)       |                 |
| .items()                                                            |           |               | O(1)       |                 |
| .fromkeys()                                                         |           |               | O(n)       |                 |
|                                                                     |           |               |            |                 |
| ---- Iterators() -------------------------------------------------- |           |               |            |                 |
| previous(i)                                                         | -         | -             | -          | -               |
| next(i)                                                             | -         | -             | -          | -               |
| start(i)                                                            | -         | -             | -          | -               |
| end(i)                                                              | -         | -             | -          | -               |

  
