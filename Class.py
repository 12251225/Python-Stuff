<<<<<<< HEAD



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



=======



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



>>>>>>> fbca7da7abe4ab3d4609abfd3dad9c5f7cbf0209
