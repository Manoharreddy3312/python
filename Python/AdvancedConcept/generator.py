''' 
it is a function it is used to generate/create collection using yield keyword

'''
# def func():
#     return 10
# print("hellow")

# print(func())
# def func2():
#     yield 10
#     print("hello")
#     yield 20
#     yield 30
#     print("world")
#     return 40
#     print("python")
# print(list(func2()))
# print(func2())


def numbers(n):
    for i in range(1,n+1):
        yield i
print(list(numbers(5)))





















