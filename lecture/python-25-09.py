def add(*args):
    print(args)
add(2, 3, 4, 5)

def greeting(**kwargs):
    print(kwargs)
greeting(apple = 12, banana = 12)