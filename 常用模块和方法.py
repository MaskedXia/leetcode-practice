# itertools系列
from itertools import permutations, combinations
a = [1,2,3]
pe = list(permutations(a))
#排列[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
com = list(combinations(a,2))
#组合[(1, 2), (1, 3), (2, 3)]



# collections系列
from collections import Counter, deque, defaultdict
#计数器(Counter)
a = [1,2,1,1,2,3,3,3,3]
a_count = Counter(a)

#Counter({3: 4, 1: 3, 2: 2})
#双向队列(deque)
a_deque = deque(a)
a_deque.popleft()
#deque([2, 1, 1, 2, 3, 3, 3, 3])

#默认字典(defaultdict)
a = [1,2,1]
hash_list = defaultdict(list)#列表字典
for i in range(3):
    hash_list[a[i]].append('*')
#defaultdict(<class 'list'>, {1: ['*', '*'], 2: ['*']})
hash_int = defaultdict(int)#用来计数
for k in a:
    hash_int[k] += 1
#defaultdict(<class 'int'>, {1: 2, 2: 1})
hash_set = defaultdict(set)#集合字典
for i in range(3):
    hash_set[a[i]].add('*')
#defaultdict(<class 'set'>, {1: {'*'}, 2: {'*'}})

