def echo():
    while True:
        received = yield
        print(f"Received: {received}")


# create an object


gen = echo()
next(gen)

gen.send("Hello")
gen.send("World")
