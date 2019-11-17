from datetime.date_time import dt
print(dt)
def f1(func):
    def inner_fun():
        print("Running f1 program")
    return inner_fun
@f1
def f11():
    print("Running f11 program")
f11()
def f2(func):
    def inner_fun():
        print("Running f2 program")
    return inner_fun
@f1
@f2
def f12():
    print("Running f12 program")
f12()
def f3(func):
    def inner_fun():
        print("Running f3 program")
    return inner_fun
@f1
@f2
@f3
def f13():
    print("Running f13 program")
f13()


