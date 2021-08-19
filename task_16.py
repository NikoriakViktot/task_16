#task1
# Create your own implementation of a built - in function enumerate, named
# `with_index`, which takes two parameters: `iterable` and `start`, default is 0.
# Tips: see the documentation for the enumerate function

l1 = ['один','два','три']
start = 1
def with_index(iterable, start):
 a_list = []
 for i in range(len(iterable)):
    a_list.append((i + start, iterable[i]))
 return a_list
print(with_index(l1, start))
print('Я функція enumerate')
print(list(enumerate(l1, 1)))


#task2
# Create your own implementation of a built-in function range, named in_range(), which takes
# three parameters: `start`, `end`, and optional step.
# Tips: See the documentation for `range` function

def in_range(start,end,step):
     print(start)
     while start + step < end:
        start += step
        print(start)
in_range(10,20,1)
print('Я функція range')
x = range(10, 20, 1)
for n in x:
    print(n)




#task3
# Create your own implementation of an iterable, which could be used inside for-in loop.
# Also, add logic for retrieving elements using square brackets syntax.
print('Я функція iter')
def iterable(low, high):
    current = low
    while current < high:
        yield current
        current += 1

for c in iter(iterable(1, 4)):
    print(c)

my = ("oдин", "два", "три")
for x in my:
    print(x)
my_iter = iter(my)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


