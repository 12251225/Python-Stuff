


class test():
    def func(self,x):
        print(x)
    def func2(self,y):
        print(y)

class test1(test):
    def func(self,x):
        print("This is the second class")
        test.func()

t=test()
b=test1()
t.func(1)
t.func2(2)
b.func()



