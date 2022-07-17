def func1():
    param =4

    def inner():
        param +=1

    return param

def func2():
    param = 4
    
    def inner(var):
        var +=1

    inner(param)
    return param

def func3():
    param = 4

    def inner(var):
        var +=1
        return var

    param = inner(param)
    return param

print(func1())
print(func2())
print(func3())
# func1() Во внутренней функции внешняя переменная не доступна, но так как мы ее 
# не вызывали - ошибки нет.
# func2() Внутренняя функция увеличила значение на 1, но сама ничего не возвращает (кроме None),
#поэтому значение param не изменилось.
# func3() Во внутренней функции увеличили внешнюю переменную и присвоили результат в func3().
# В результате вернулось 5.