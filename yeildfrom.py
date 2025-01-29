def subgenerator():
    yield 1
    yield 2
    yield 3


def maingenerator():
    yield from subgenerator()
    yield 4
    yield 5


for value in maingenerator():
    print(value)
