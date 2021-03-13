def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y

print(add(3,4))

#print(bool())

foo = []
if foo:
    print(foo)
elif foo == []:
    print('100% sure foo is empty')
else:
    print('what hell?')

def add(x):
    def addX(y):
        print(x)
        print(y)
        return y + x
    return addX
foo = add(1)
print(foo(2))

li = [1, 2, 3, 4, 5, 6, 7, 8];
print(li[0:7:4])

a = [1,2]
b = a
c = [1,2]
d = a[:]
print(b == a)
print(b is a)
print(c == a)
print(c is a)
print(d == a)
print(d is a)

a = (1, 2, 3, 4, 5)
b, *c, d = a;
print(b,c,d)

li = [];
tu = ();
dic = {};
s = set();

new_list = [1,2,3,4,5]
new_tuple = (1,2,3,4,5)
new_dic = {'a':1,'b':2}
new_set = {1,2,3,4,5,1,2,3,4,5}
other_list = [6,7,8]

#print(new_list,new_tuple,new_dic,new_set)

new_list.extend([1,2,3])
print(new_list)

def tupleArgs(*args):
    t = args
    print(t)
    print(t == (1,2,3))

tupleArgs(1,2,3)


