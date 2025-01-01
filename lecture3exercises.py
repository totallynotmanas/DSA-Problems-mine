'''
#exercise 1
x='global'
def f():
    x='enclosing'
    def g():
        x='local'
        print(x)
    g()
    print(x)
f()
print(x)
'''
'''
#exerrcise 2
def f():
    x='enclosing'
    def g():
        x='local'
        print(x)
    g()
f()
'''
'''
#excercise 3
print(global())
def f(x,y):
    s= 'foo' 
    print(locals())
f(10,0.5)
'''