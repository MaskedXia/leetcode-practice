class A(object):
    __instance = None #定义一个类属性用作判断
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance == object.__new__(cls) #如果为空，第一次创建实例，通过父类创建
            return cls.__instance
        else:
            return cls.__instance#返回上一个对象的引用

a = A()
print(id(a))
b = A()
print(id(b))