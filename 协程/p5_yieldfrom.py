#yield from

def ex1():
    yield 1
    yield 2
    return 3

def ex2():
    ex1_result = yield from ex1()
    print(f'ex1 : {ex1_result}')
    yield None

gen1 = ex1()
gen1.send(None)#1
gen1.send(None)#2
gen1.send(None)# send 执行到return 返回 StopIteration :3

for i in ex2():
    print(i)

#1
#2
#ex1:3
#None

#########
def bottom():
    return (yield 42)

def middle():
    return (yield from bottom())

def top():
    return (yield from middle())

gen = top()
value = next(gen)
print(value)
try:
    value = gen.send(value * 2)
except StopIteration as exc:
    value = exc.value
print(value)