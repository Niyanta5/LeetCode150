def prime(alist):
    for num in alist:
        if num > 1:
            for i in range(2, int(num ** (1 / 2)) + 1):
                if num % i == 0:
                    break
            else:
                yield num


primo = prime([2, 4, 3, 21, 3, 42, 32])

for value in primo:
    print(value)
