alist=[1,2,3,4,5]
hasattr(alist,'__iter__')#True
hasattr(alist,'__getitem__')#True
hasattr(alist,'__next__')#False
#实现这三个是完整迭代器

# for i in alist:

#结论一 列表是可迭代对象，或称作可迭代（iterable）
#       不是迭代器（iterator）

g = (i for i in range(5))
#生成器

hasattr(g,'__iter__')#True
hasattr(g,'__next__')#True

# g.__next__()
# next(g)
# for i in g:
#     i
#结论2 生成器可以实现完整的迭代器协议
#类实现完整的迭代器协议


'''
存几个固定的数据，反复使用	列表（可迭代对象）	[1, 2, 3]
需要从某处依次取数据，但只想取一次	迭代器（或直接 for 循环）	for line in file: 文件本身是迭代器
数据量很大（比如几百万个数），不想占内存	生成器	(x*x for x in range(10**7))
需要无限序列（比如随机数流）	生成器	while True: yield random.random()
自定义一个“能一个一个吐东西”的逻辑	生成器函数（最简单）	上面那些 yield 的例子
'''
#迭代器
p = [1, 2, 3]
s = iter(p)    # 手伸进箱子里
print(next(s))     # 拿第一个 → 1
print(next(s))     # 拿第二个 → 2
print(next(s))     # 拿第三个 → 3
# print(next(s))     # 箱子里没了 → 报错 StopIteration


#生成器
def z():
    for i in range(3):
        yield f"苹果{i}"   # 造一个，给出去，然后暂停等我下次再要

j = z()          # 机器建好了，还没开始生产
print(next(j))        # 造第一个苹果0
print(next(j))        # 造第二个苹果1
print(next(j))        # 造第三个苹果2





