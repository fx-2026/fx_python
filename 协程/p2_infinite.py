#itertools的三个常见无限迭代器

import itertools
count =itertools.count()#计数器
next(count)
next(count)
next(count)


cycle =itertools.cycle(('yes','no'))
next(cycle)


repeat= itertools.repeat(10,times =2)
next(repeat)


#有限迭代器
for j in itertools.chain('ABC',[1,2,3]):
    j

def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i

s ='ABC'
t=[1,2,3]
list(chain(s,t))


def chain2(*iterables):
    for i in iterables:
        yield from i#代替内层循环

list(chain2(s,t))